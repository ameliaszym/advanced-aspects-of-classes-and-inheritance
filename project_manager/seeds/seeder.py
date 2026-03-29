class Seeder:
    def __init__(self, team_service, task_service, comment_service):
        self.team_service = team_service
        self.task_service = task_service
        self.comment_service = comment_service

    def seed(self):
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