import os
from models.tasks.tasks import AdvancedTask

class TaskCLI:
    def __init__(self, task, task_service):
        self.task = task
        self.task_service = task_service

    def run(self):
        while True:
            print(f"\n=== Task: {self.task.title} [{self.task.get_type()}] [{"✔" if self.task.completed else "✘"}] ===")
            if hasattr(self.task, 'show_mro'): print(f"Resolution order: {' -> '.join(self.task.show_mro())}")
            comments = self.task.show_comments()
            if comments:
                print('Comments:')
                for c in comments: print(f"\t- {c}")
            else: print("No comments yet.")
            print("\na. Add comment \nb. Complete task \nq. Quit")
            choice = input("> ").strip().lower()
            if choice == "q": break
            elif choice == "a":
                content = input("Comment: ").strip()
                if content:
                    self.task_service.add_comment(self.task, content)
                    print("Comment added.")
            elif choice == "b":
                if self.task.completed:
                    os.system('cls') 
                    print("Task already completed.")
                else: print(self.task_service.complete_task(self.task))
            else:
                os.system('cls')
                print("Invalid option!")