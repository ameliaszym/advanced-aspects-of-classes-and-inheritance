from models.tasks.advanced_task import AdvancedTask

class TaskCLI:
    def __init__(self, task, task_service, comment_service):
        self.task = task
        self.task_service = task_service
        self.comment_service = comment_service

    def run(self):
        while True:
            task_type = self.task.get_type()
            print(f"\n=== Task: {self.task.title} [{task_type}] ===")
            if isinstance(self.task, AdvancedTask):
                print(f"  Resolution order: {' -> '.join(self.task.show_mro())}")
            comments = self.task.show_comments()
            if comments:
                for c in comments: print(f" - {c}")
            else: print(" No comments yet.")
            print("a. Add comment \nb. Complete task \nq. Quit")
            choice = input("> ").strip().lower()
            if choice == "q": break
            elif choice == "a":
                content = input("Comment: ").strip()
                if content:
                    self.comment_service.add_comment(self.task, content)
                    print("Comment added.")
            elif choice == "b":
                if self.task.completed:
                    print("Task already completed.")
                else: print(self.task_service.complete_task(self.task))
            else: print("Invalid option.")