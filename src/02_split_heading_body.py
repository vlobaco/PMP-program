import pickle
import re

## This module will load the contents
## in the pickle file

## path to the pickle file
path = 'data/contents.pkl'

## load the contents
with open(path, 'rb') as file:
    contents = pickle.load(file)

print(f"Loaded {len(contents)} contents.")

## This module will split each content into
## heading and body.
##
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
## In order to split the contents, we carry out a split
## operation on the <number of items already completed>/<total number of items>
## part of the heading.
## Special consideration must be given to the spaces
## between the numbers and the slash.

# split the contents into heading and body, using
# the <number of items already completed>/

split_re = re.compile(r'((.+\n){,3}\d{1,2} ?\/.+?)\n')
headings = []
bodies = []
for content in contents:
    splits = split_re.split(content, maxsplit=1)
    heading = splits[1].strip()
    body = splits[-1].strip()
    headings.append(heading)
    bodies.append(body)

## This module will save the headings and bodies
## into separate pickle files.

## path to the pickle files
heading_path = 'data/headings.pkl'
body_path = 'data/bodies.pkl'

## save the headings
with open(heading_path, 'wb') as file:
    pickle.dump(headings, file)
with open(body_path, 'wb') as file:
    pickle.dump(bodies, file)

print(f"Saved {len(headings)} headings and {len(bodies)} bodies.")