import os
from cli.member_tasks_cli import MemberTasksCLI

class TeamCLI:
    def __init__(self, project, task_service, comment_service):
        self.project = project
        self.task_service = task_service
        self.comment_service = comment_service

    def run(self):
        if not self.project.team:
            print("No team members.")
            return
        while True:
            print("\n=== Team Members ===")
            for i, member in enumerate(self.project.team): print(f"{i}: {member.display()}")
            print("q. Quit")
            choice = input("> ").strip().lower()
            if choice == "q": break
            try: MemberTasksCLI(self.project.team[int(choice)], self.task_service, self.comment_service).run()
            except (ValueError, IndexError):
                os.system('cls')
                print("Invalid member selection!")