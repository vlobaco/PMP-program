## This module will define the structure of the lessons

class Lesson:
    def __init__(self, lesson, title, length, section):
        self.lesson = lesson
        self.title = title
        self.length = length
        self.section = section

    def __str__(self):
        return f"{self.lesson + ". " if self.lesson else ''}{self.title} | {str(self.length)+'min' if self.length else 'None'}"
    
    def __repr__(self):
        return f"{self.lesson + ". " if self.lesson else ''}{self.title} | {str(self.length)+'min' if self.length else 'None'}"