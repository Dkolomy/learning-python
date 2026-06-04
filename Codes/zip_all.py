# Your goal is to implement a function, zip_all(), that takes three input arguments 
# for a path to the top-level directory you want to include, a list of file extensions, 
# and an output file path for the resulting archive.

# The 'os' module in Python provides a way of using operating system dependent functionality 
# such as reading or writing to the file system, traversing directories, and handling file paths.
# It is commonly used to work with directories and files programmatically.
import os

# The 'zipfile' module in Python provides tools for creating, reading, writing, 
# appending, and listing ZIP files. The 'ZipFile' class is used to work with ZIP archives. 
# You can use it to write files into a ZIP archive or extract files from one.
from zipfile import ZipFile

def zip_all(top_dir, extensions, output_path):
  with ZipFile(output_path, 'w') as zip_output:
    for dirpath, dirnames, filenames in os.walk(top_dir):
      rel_path = os.path.relpath(dirpath, top_dir)
      for file in filenames:
        _, ext = os.path.splitext(file)
        if ext.lower() in extensions:
          zip_output.write(os.path.join(dirpath, file), arcname=os.path.join(rel_path, file))

zip_all('test_dir', ['.txt', '.py'], 'test_dir.zip')