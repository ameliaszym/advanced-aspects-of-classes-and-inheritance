import os
from cli.task_cli import TaskCLI
from services.task_service import TASK_TYPES

class MemberTasksCLI:
    def __init__(self, member, task_service):
        self.member = member
        self.task_service = task_service

    def run(self):
        while True:
            print(f"\n=== Tasks assigned to {self.member.display()} ===")
            if self.member.assigned_tasks:
                for i, task in enumerate(self.member.assigned_tasks): print(f"{i}: {task.title} [{task.get_type()}] [{"✔" if task.completed else "✘"}]")
            else: print("\tNo tasks assigned yet.")
            print("\na. Add new task\nq. Quit")
            choice = input("> ").strip().lower()
            if choice == "q": break
            elif choice == "a": self._add_task()
            else:
                try: TaskCLI(self.member.assigned_tasks[int(choice)], self.task_service).run()
                except (ValueError, IndexError):
                    os.system('cls')
                    print("Invalid task selection!")

    def _add_task(self):
        title = input("Task title: ").strip()
        if not title:
            os.system('cls')
            print("Title cannot be empty.")
            return
        allowed = self.task_service.allowed_task_types(self.member)
        task_type = input(f"Type ({'/'.join(sorted(allowed))}): ").strip().lower()
        try:
            self.task_service.add_task(title, self.member, task_type)
            print("Task created successfully.")
        except (ValueError, PermissionError) as e:
            os.system('cls')
            print(f"Cannot create task: {e}")