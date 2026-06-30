import os
from pathlib import Path
# Define the folder where your documents will live
docs_folder = Path ("docs")

# Creates doc folder, net new
docs_folder.mkdir(exist_ok=True)

#Get all files within doc folder
files = list(docs_folder.iterdir())

#print contents
for file in files:
    print(file.name)

#Read and print file content
for file in files:
    print(f"\n-- Reading {file.name} ---")
    with open(file, "r") as f:
        content = f.read()
    print(content[:500])

