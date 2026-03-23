from .base_task import Task

class FeatureTask(Task):
    def __init__(self, title, member):
        super().__init__(title, member)

    def complete(self):
        return super().complete() + " (feature added)"

    def get_type(self):
        return "feature"