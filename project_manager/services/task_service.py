from models.tasks.bug_task import BugTask
from models.tasks.feature_task import FeatureTask
from models.tasks.advanced_task import AdvancedTask

TASK_TYPES = {"bug", "feature", "advanced"}

class TaskService:
    def __init__(self, project):
        self.project = project

    def add_task(self, title, member, task_type):
        if not member.role.can_create_task_type(task_type):
            allowed = self._allowed_types_for(member)
            raise PermissionError(
                f"{member.display()} cannot create '{task_type}' tasks. "
                f"Allowed types: {', '.join(allowed)}."
            )
        task_map = {
            "bug": BugTask,
            "feature": FeatureTask,
            "advanced": AdvancedTask
        }
        task = task_map[task_type](title, member)
        self.project.add_task(task)
        return task

    def complete_task(self, task):
        return task.complete()