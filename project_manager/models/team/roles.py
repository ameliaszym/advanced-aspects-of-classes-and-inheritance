class Role:
    def get_name(self):
        return "role"
 
    def get_max_tasks(self):
        return None
 
    def can_create_task_type(self, task_type):
        return True

class Developer(Role):
    def get_name(self):
        return "Developer"
 
    def get_max_tasks(self):
        return 5
 
    def can_create_task_type(self, task_type):
        return task_type in {"bug", "feature"}

class Tester(Role):
    def get_name(self):
        return "Tester"
 
    def get_max_tasks(self):
        return 3
 
    def can_create_task_type(self, task_type):
        return task_type in {"bug"}

class Manager(Role):
    def get_name(self):
        return "Manager"
 
    def get_max_tasks(self):
        return None
 
    def can_create_task_type(self, task_type):
        return task_type in {"bug", "feature", "advanced"}