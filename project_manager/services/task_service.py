from models.tasks.tasks import BugTask, FeatureTask, AdvancedTask

TASK_MAP = {"bug": BugTask, "feature": FeatureTask, "advanced": AdvancedTask}
TASK_TYPES = frozenset(TASK_MAP) # Exported task types set

class TaskService:
    def __init__(self, project):
        self.project = project
    
    def allowed_task_types(self, member) -> frozenset[str]:
        return frozenset(t for t in TASK_TYPES if member.role.can_create_task_type(t))

    def add_task(self, title, member, task_type):
        if task_type not in TASK_TYPES: raise ValueError(f"Unknown task type: '{task_type}'.")
        if not member.role.can_create_task_type(task_type): raise PermissionError(f"{member.display()} cannot create '{task_type}' tasks. Allowed types: {', '.join(self.allowed_task_types(member))}." )
        task = TASK_MAP[task_type](title, member)
        member.assign_task(task)
        self.project.add_task(task)
        return task

    def complete_task(self, task):
        return task.complete()
    
    def add_comment(self, task, content):
        task.add_comment(content)