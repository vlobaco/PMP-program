from body import Body
from functools import total_ordering

## This module will define the structure of a section

@total_ordering
class Section:
    def __init__ (self, heading):
        self.heading = heading
        self.body = Body()

    def __str__(self):
        return f"{self.heading}"
    
    def __repr__(self):
        return f"{self.heading}"
    
    def __lt__(self, other):
        if isinstance(other, Section):
            return self.heading.section < other.heading.section
        
    def __eq__(self, other):
        if isinstance(other, Section):
            return self.heading.section == other.heading.section