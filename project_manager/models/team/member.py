class TeamMember:
    member_count = 0                    # zmienna klasowa

    def __init__(self, name, role):     # zmienne instancyjne
        self.name = name
        self.role = role
        self.assigned_tasks = []
        self.completed_tasks = []
        TeamMember.member_count += 1

    def assign_task(self, task):        # metoda instancyjna
        max_tasks = self.role.get_max_tasks()
        if max_tasks is not None and len(self.assigned_tasks) >= max_tasks:
            raise ValueError(
                f"{self.display()} has reached the task limit "
                f"({max_tasks} active tasks allowed for {self.role.get_name()})."
            )
        self.assigned_tasks.append(task)

    def complete_task(self, task):
        self.assigned_tasks.remove(task)
        self.completed_tasks.append(task)

    def get_task_summary(self):
        max_tasks = self.role.get_max_tasks()
        limit_str = str(max_tasks) if max_tasks is not None else "∞"
        return (
            f"active: {len(self.assigned_tasks)}/{limit_str}, "
            f"completed: {len(self.completed_tasks)}"
        )

    def display(self):                  # polimorfizm
        return f"{self.role.get_name().lower()}: {self.name}"

    @classmethod
    def get_member_count(cls):
        return cls.member_count

    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and len(name) > 0