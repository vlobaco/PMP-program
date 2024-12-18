## This module will define the structure of the headings

class Heading:
    def __init__(self, section, title, items, length):
        self.section = section
        self.title = title
        self.items = items
        self.length = length

    def __str__(self):
        return f"Section {self.section}: {self.title}\n{self.items} | {self.length}min"

    def __repr__(self):
        return f"Section {self.section}: {self.title}\n{self.items} | {self.length}min"