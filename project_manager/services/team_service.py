from models.team.member import TeamMember
from models.team.roles import Developer, Tester, Manager

class TeamService:
    def __init__(self, project):
        self.project = project

    def add_member(self, name, role_type):
        role_map = {
            "developer": Developer,
            "tester": Tester,
            "manager": Manager
        }
        role_class = role_map.get(role_type)
        if role_class is None:
            raise ValueError(f"Unknown role type: '{role_type}'.")
        role = role_class()
        member = TeamMember(name, role)
        self.project.add_member(member)
        return member