import os
from models.project import Project
from models.team.member import TeamMember
from services.team_service import TeamService, ROLE_MAP
from services.task_service import TaskService
from cli.team_cli import TeamCLI
from seeds.seeder import Seeder

class ProjectManagerCLI:
    def __init__(self):
        self.project = Project("Python project")
        self.team_service = TeamService(self.project)
        self.task_service = TaskService(self.project)

        seeder = Seeder(self.team_service, self.task_service)
        seeder.seed()

    def run(self):
        while True:
            print("\n=== Project Manager CLI ===\n1. Add team member\n2. Show team members\n3. Show project report\nq. Exit")
            choice = input("> ").strip()
            match choice:
                case '1': self._add_team_member()
                case '2': TeamCLI(self.project, self.task_service).run()
                case '3': self._show_project_report()
                case 'q': break
                case _:
                    os.system('cls')
                    print("Invalid option!")

    def _add_team_member(self):
        name = input("Name: ").strip()
        if not name:
            os.system('cls')
            print("Name cannot be empty.")
            return
        if not TeamMember.validate_name(name):
            os.system('cls')
            print("Invalid name format.")
            return
        role = input(f"Role ({'/'.join(sorted(set(ROLE_MAP)))}): ").strip().lower()
        try:
            self.team_service.add_member(name, role)
            print("Team member added successfully.")
        except ValueError:
            os.system('cls')
            print(f"Invalid role. Choose from: {', '.join(ROLE_MAP)}")

    def _show_project_report(self):
        print(f"\n=== Project Report for: {self.project.name} ===\nTeam size: {TeamMember.get_member_count()} member(s)\nProject progress: {self.project.get_project_progress()}\n\n--- All Tasks ---")
        if not self.project.tasks:
            print("No tasks in the project.")
            return
        for i, task in enumerate(self.project.tasks):
            print(f"{i}: {task.title} [{task.get_type()}]\n\tAssigned to {task.assigned_member.display()} ({task.assigned_member.get_task_summary()})\n\tCompleted: [{"✔" if task.completed else "✘"}]")
            comments = task.show_comments()
            if comments:
                print("\tComments:")
                for c in comments: print(f"\t\t{c}")
            else: print("\tNo comments")