from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, title, member):
        self.title = title
        self.assigned_member = member
        self.completed = False
        self.comments = []
        member.assign_task(self)

    def add_comment(self, comment):
        self.comments.append(comment)

    def show_comments(self):
        return [c.display() for c in self.comments]

    def complete(self):
        self.completed = True
        self.assigned_member.complete_task(self)
        return f"Task '{self.title}' completed"

    @abstractmethod
    def get_type(self): pass

    def __str__(self):
        return f"[{'✔' if self.completed else '✘'}] {self.title}"