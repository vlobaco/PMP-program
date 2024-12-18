from lesson import Lesson
import csv
import pickle
import re

## This module will load the bodies
## in the pickle file

# path to the pickle file
bodies_path = 'data/bodies.pkl'

# load the bodies
with open(bodies_path, 'rb') as file:
    bodies = pickle.load(file)

print(f"Loaded {len(bodies)} bodies.")

## This module will load the sections
## in the pickle file

# path to the pickle file
sections_path = 'data/sections.pkl'

# load the sections
with open(sections_path, 'rb') as file:
    sections = pickle.load(file)

## This module will process the bodies. A body 
## can be split into lessons. Each lesson takes
## exactly two lines.
## The first line contains optionally the number of the lesson:
## <number of lesson>. <title>
## followed by a point,
## The second line contains the length of the lesson:
## <number of minutes>min
##
## In order to process the bodies, the number of lessons 
## and the length must match

split_first_line = re.compile(r'(\d{1,3}\. ?)')
split_second_line = re.compile(r'(\d{1,2}min)')
split_unique_line = re.compile(r'\W+(.+)')
for section_index, body in enumerate(bodies):
    body_lines = body.split('\n')
    section_class = sections[section_index]
    section = section_class.heading.section
    body_line_index = 0
    section_class.body.lessons = []
    while body_line_index < len(body_lines):
        first_line = body_lines[body_line_index]
        splits_first_line = split_first_line.split(first_line)
        if len(splits_first_line) < 2:
            lesson = None
            title = split_unique_line.split(first_line)[1]
            length = None
        else:
            lesson = splits_first_line[1].split('.')[0]
            title = splits_first_line[2]
            while True:
                second_line = body_lines[body_line_index + 1]
                splits_second_line = split_second_line.split(second_line)
                body_line_index += 1
                if len(splits_second_line) < 2:
                    title += ' ' + second_line
                else:
                    break
            length = int(splits_second_line[1][:-3])
        lesson = Lesson(lesson, title, length, section)
        section_class.body.lessons.append(lesson)
        body_line_index += 1

    ## Check if the number of lessons and the length match
    number_of_lessons = len(section_class.body.lessons)
    total_length = sum([lesson.length for lesson in section_class.body.lessons if lesson.length])
    if number_of_lessons != section_class.heading.items or abs(total_length - section_class.heading.length)>1:
        print(f"Section '{section_class.heading.title}' has {number_of_lessons} lessons and a total length of {total_length} minutes.")
        print(f"Expected {section_class.heading.items} lessons and a total length of {section_class.heading.length} minutes.")


# Save the processed headings
with open('data/sections.pkl', 'wb') as file:
    pickle.dump(sections, file)

# Save the lessons as csv
csv_path = 'data/lessons.csv'
lessons = [lesson for section in sections for lesson in section.body.lessons]

with open(csv_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=lessons[0].__dict__.keys())
    writer.writeheader()
    for lesson in lessons:
        writer.writerow(lesson.__dict__)

print(f"Saved {len(lessons)} lessons in {csv_path}.")