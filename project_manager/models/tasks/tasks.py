from .base_task import Task
from datetime import datetime

# --- Mixins ---

class LoggerMixin:
    def complete(self):
        print(f"  [LOG] Completing task: '{self.title}'")
        result = super().complete()       # cooperative inheritance
        print(f"  [LOG] Result: {result}")
        return result

class TimestampMixin:
    def complete(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"  [TIMESTAMP] Completed at: {now}")
        return super().complete()       # cooperative inheritance

# --- Task types ---

class BugTask(Task):
    def __init__(self, title, member):
        super().__init__(title, member)

    def complete(self):         # nadpisywanie z rozszerzeniem
        return super().complete() + " (bug fixed)"

    def get_type(self):
        return "bug"
    
class FeatureTask(Task):
    def __init__(self, title, member):
        super().__init__(title, member)

    def complete(self):
        return super().complete() + " (feature added)"

    def get_type(self):
        return "feature"

class AdvancedTask(LoggerMixin, TimestampMixin, Task):
    def __init__(self, title, member):
        super().__init__(title, member)

    def get_type(self):
        return "advanced"

    @classmethod
    def show_mro(cls):
        return [c.__name__ for c in cls.__mro__]        # MRO