'''
Generates a CSV file listing all files in the current directory and all subdirectories.
Directories are listed before the files in that directory.
Filenames are stripped of their file suffix.

The CSV file is saved to the current directory with the name "DirectoryListing.csv".
This file must be run in the root directory of the files to be listed.
'''

import os
import csv

# Get the current working directory
current_dir = os.getcwd()

# Create a list to store all the file names
file_list = []

# Walk through all directories and files in the current directory
for dirpath, dirnames, filenames in os.walk(current_dir):
    # Add each file name to the file list
    for filename in filenames:
        # Get the file name without the file suffix
        file_name = os.path.splitext(filename)[0]
        file_list.append(file_name)

# Write the file list to a CSV file
with open('DirectoryListing.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Directory Name', 'File Name'])
    # Loop through each directory and its files and write them to the CSV file
    for dirpath, dirnames, filenames in os.walk(current_dir):
        # Write the directory name before the files in this directory
        writer.writerow([dirpath, ''])
        for filename in filenames:
            # Get the file name without the file suffix
            file_name = os.path.splitext(filename)[0]
            # Write the file name to the CSV file
            writer.writerow(['', file_name])

print(f"Directory listing has been saved to {os.path.join(current_dir, 'DirectoryListing.csv')}")
