from heading import Heading
from section import Section
import pickle
import re

## This module will load the headings
## in the pickle file

## path to the pickle file
headings_path = 'data/headings.pkl'

## load the headings
with open(headings_path, 'rb') as file:
    headings = pickle.load(file)

print(f"Loaded {len(headings)} headings.")

## This module will process the headings
## The structure of the headings is as follows:
##
## Section <section number>: <title>
## <number of items already completed>/<total number of items> | <length>
##
## Everyline after the heading is considered as the body of the section.
## The title can span multiple lines.
## The | can have been recorded as a different character.
## The length follows the format <number of hours>hr <number of minutes>min,
## and the hours and minutes are optional.
##
## In order to process the headings, we carry out a split
## operation on the <number of items already completed>/<total number of items>

split_re = re.compile(r'Section (\d{1,2}): ([\w\W]+)\n\d{1,2} ?\/ ?(\d{1,2}) ')
split_duration = re.compile(r'(\d ?hr|\d{1,2} ?min)')
sections = []
for heading_description in headings:
    splits = split_re.split(heading_description)
    section = int(splits[1])
    title = splits[2].replace("\n", " ").strip()
    items = int(splits[3])
    length_str = splits[4]
    length_splits = split_duration.split(length_str)
    length = 0
    for split in length_splits[1:]:
        if split.endswith("hr"):
            length = int(split[0]) * 60
        elif split.endswith("min"):
            length += int(split[:-3])
            break
    heading = Heading(section, title, items, length)
    section = Section(heading)
    sections.append(section)


## Save the processed headings
with open('data/sections.pkl', 'wb') as file:
    pickle.dump(sections, file)

print(f"Processed {len(sections)} headings.")