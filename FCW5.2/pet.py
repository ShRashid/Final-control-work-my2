from typing import List

class Pet:
    def __init__(self, name: str, pet_class: str):
        self.name = name
        self.pet_class = pet_class
        self.commands: List[str] = []

    def add_command(self, command: str):
        self.commands.append(command)

    def get_commands(self) -> List[str]:
        return self.commands
