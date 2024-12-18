from body import Body

## This module will define the structure of a section

class Section:
    def __init__ (self, heading):
        self.heading = heading
        self.body = Body()

    def __str__(self):
        return f"{self.heading}\n{self.body}"
    
    def __repr__(self):
        return f"{self.heading}\n{self.body}"