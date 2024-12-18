from os import path, walk
import pickle

## This module will read the files in the 
## txt directory, creating a list of the 
## files names and their paths.

## The path to the directory
directory = "txt"

## The list of files
files = []

## Loop through the files in the directory
for root, dirs, filenames in walk(directory):
    for filename in filenames:
        files.append(path.join(root, filename))

print(f"Found {len(files)} files in the directory.")

## This module will read the files in the
## txt directory, adding the contents of
## each file to a list.

## The list of file contents
contents = []

## Loop through the files
for file in files:
    with open(file, "r") as f:
        content = f.read()
        # Replace any tabs with spaces
        content = content.replace("\t", " ")
        contents.append(content)

print(f"Read {len(contents)} files.")

## This module will save the list of file
## contents to a file using the pickle module.

# The path to the file
file = "data/contents.pkl"

# Save the contents to the file
with open(file, "wb") as f:
    pickle.dump(contents, f)

print(f"Saved the contents to {file}.")