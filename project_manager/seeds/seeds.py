def seed(team_service, task_service):
    alice = team_service.add_member("Alice", "developer")
    bob = team_service.add_member("Bob", "tester")
    carol = team_service.add_member("Carol", "manager")

    task1 = task_service.add_task("Implement login", alice, "feature")
    task2 = task_service.add_task("Fix signup bug", bob, "bug")
    task3 = task_service.add_task("Design dashboard", carol, "advanced")

    task_service.add_comment(task1, "Remember to use secure password hashing.")
    task_service.add_comment(task1, "Add unit tests for login.")
    task_service.add_comment(task2, "Bug appears only on mobile.")
    task_service.add_comment(task3, "Dashboard should support dark mode.")

    task_service.complete_task(task2)