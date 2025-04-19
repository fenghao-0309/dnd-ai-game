import random

class Character:
    def __init__(self, name, role, attributes, skills):
        self.name = name
        self.role = role
        self.attributes = attributes  # e.g., {"Academic Pressure": 5}
        self.skills = skills          # e.g., {"Grade Negotiation": 3}

    def perform_skill(self, skill_name):
        skill_level = self.skills.get(skill_name, 0)
        roll = random.randint(1, 20)
        success = roll + skill_level
        return roll, success
