class Project:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.tasks = []

    def add_member(self, member):
        self.team.append(member)

    def add_task(self, task):
        self.tasks.append(task)

    def get_project_progress(self):
        total = len(self.tasks)
        done = sum(t.completed for t in self.tasks)
        return f"{(done / total * 100):.2f}%" if total else "No tasks"