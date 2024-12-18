## This module will define the structure of the bodies

class Body:
    def __init__(self):
        self.lessons = []

    def __str__(self):
        return f"Body: {self.lessons}"