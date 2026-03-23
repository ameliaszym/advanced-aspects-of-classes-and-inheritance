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
            for i, m in enumerate(self.project.team):
                print(f"{i}: {m.display()}")
            print("q. Quit")
            choice = input("> ").strip()
            if choice.lower() == "q": break
            try:
                member_index = int(choice)
                member = self.project.team[member_index]
                MemberTasksCLI(member, self.task_service, self.comment_service).run()
            except (ValueError, IndexError):
                print("Invalid member selection.")