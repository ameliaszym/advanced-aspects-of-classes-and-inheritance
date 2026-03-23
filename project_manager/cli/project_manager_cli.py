from models.project import Project
from services.team_service import TeamService
from services.task_service import TaskService
from services.comment_service import CommentService
from cli.team_cli import TeamCLI
from models.team.member import TeamMember

class ProjectManagerCLI:
    def __init__(self):
        self.project = Project("Demo Project")
        self.team_service = TeamService(self.project)
        self.task_service = TaskService(self.project)
        self.comment_service = CommentService()
        self._create_sample_data()

    def _create_sample_data(self):
        alice = self.team_service.add_member("Alice", "developer")
        bob = self.team_service.add_member("Bob", "tester")
        carol = self.team_service.add_member("Carol", "manager")

        task1 = self.task_service.add_task("Implement login", alice, "feature")
        task2 = self.task_service.add_task("Fix signup bug", bob, "bug")
        task3 = self.task_service.add_task("Design dashboard", carol, "advanced")

        self.comment_service.add_comment(task1, "Remember to use secure password hashing.")
        self.comment_service.add_comment(task1, "Add unit tests for login.")
        self.comment_service.add_comment(task2, "Bug appears only on mobile.")
        self.comment_service.add_comment(task3, "Dashboard should support dark mode.")

        self.task_service.complete_task(task2)

    def run(self):
        while True:
            print("\n=== Project Manager CLI ===")
            print("1. Add team member")
            print("2. Show team members")
            print("3. Show project report")
            print("0. Exit")
            choice = input("> ").strip()
            if choice == "1": self.add_team_member()
            elif choice == "2": TeamCLI(self.project, self.task_service, self.comment_service).run()
            elif choice == "3": self.show_project_report()
            elif choice == "0": break
            else: print("Invalid option")

    def add_team_member(self):
        name = input("Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        if not TeamMember.validate_name(name):
            print("Invalid name format.")
            return
        role = input("Role (developer/tester/manager): ").strip().lower()
        valid_roles = {"developer", "tester", "manager"}
        if role not in valid_roles:
            print(f"Invalid role. Choose from: {', '.join(valid_roles)}")
            return
        self.team_service.add_member(name, role)
        print("Team member added successfully.")

    def show_project_report(self):
        print(f"\n=== Project Report: {self.project.name} ===")
        print(f"Team size: {TeamMember.get_member_count()} member(s)")
        print(f"Project progress: {self.project.get_project_progress()}")
        print("\n--- All Tasks ---")
        if not self.project.tasks:
            print("No tasks in the project.")
            return
        for i, task in enumerate(self.project.tasks):
            status = "✔" if task.completed else "✘"
            print(f"{i}: [{status}] [{task.get_type()}] {task.title}"
                  f", assigned to {task.assigned_member.display()}"
                  f" ({task.assigned_member.get_task_summary()})")
            comments = task.show_comments()
            if comments:
                print("  Comments:")
                for c in comments:
                    print(f"   {c}")
            else: print("  No comments")