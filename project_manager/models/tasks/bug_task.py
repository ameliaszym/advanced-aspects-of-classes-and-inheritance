from .base_task import Task

class BugTask(Task):
    def __init__(self, title, member):
        super().__init__(title, member)

    def complete(self):         # nadpisywanie z rozszerzeniem
        return super().complete() + " (bug fixed)"

    def get_type(self):
        return "bug"