from cli.task_cli import TaskCLI
from services.task_service import TASK_TYPES

class MemberTasksCLI:
    def __init__(self, member, task_service, comment_service):
        self.member = member
        self.task_service = task_service
        self.comment_service = comment_service

    def run(self):
        while True:
            print(f"\n=== Tasks for {self.member.display()} ===")
            print(f"    {self.member.get_task_summary()}")
            if self.member.assigned_tasks:
                for i, task in enumerate(self.member.assigned_tasks):
                    status = "✔" if task.completed else "✘"
                    print(f"  {i}: [{status}] [{task.get_type()}] {task.title}")
            else:
                print("  No tasks assigned yet.")
            print("a. Add new task")
            print("q. Quit")
            choice = input("> ").strip()
            if choice.lower() == "q": break
            elif choice.lower() == "a":
                self.add_task_to_member()
            else:
                try:
                    task_index = int(choice)
                    task = self.member.assigned_tasks[task_index]
                    TaskCLI(task, self.task_service, self.comment_service).run()
                except (ValueError, IndexError):
                    print("Invalid task selection.")

    def add_task_to_member(self):
        title = input("Task title: ").strip()
        if not title:
            print("Title cannot be empty.")
            return
        allowed = {t for t in TASK_TYPES if self.member.role.can_create_task_type(t)}
        task_type = input(f"Type ({'/'.join(sorted(allowed))}): ").strip().lower()
        if task_type not in allowed:
            print(f"'{task_type}' is not allowed for {self.member.display()}. "
                  f"Allowed: {', '.join(sorted(allowed))}.")
            return
        try:
            self.task_service.add_task(title, self.member, task_type)
            print("Task created successfully.")
        except (ValueError, PermissionError) as e:
            print(f"Cannot create task: {e}")