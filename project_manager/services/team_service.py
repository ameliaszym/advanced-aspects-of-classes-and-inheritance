from models.team.member import TeamMember
from models.team.roles import Developer, Tester, Manager

ROLE_MAP = {"developer": Developer, "tester": Tester, "manager": Manager}

class TeamService:
    def __init__(self, project):
        self.project = project

    def add_member(self, name, role_type):
        role_class = ROLE_MAP.get(role_type)
        if role_class is None: raise ValueError(f"Unknown role type: '{role_type}'.")
        member = TeamMember(name, role_class())
        self.project.add_member(member)
        return member