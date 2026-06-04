# Your goal is to implement a function, download_files(), that takes two input arguments: 
# the URL for the first item in the sequence, and a path to the output directory where you want to save them.

# The 'os' module provides a way of interacting with the operating system,
# allowing you to read from and write to the file system, create directories,
# list files, and manipulate file paths.
import os

# The 're' module in Python is the regular expression library, which
# allows you to search for patterns in strings, extract matched substrings,
# and perform string substitutions using regular expressions.
import re

# The 'urllib.request' module allows you to open and read URLs, download files,
# and handle HTTP requests. It provides functions such as urlopen() and
# urlretrieve() to access data across the web.
import urllib.request

# The 'urllib.parse' module provides functions for breaking up URLs into
# components (such as scheme, netloc, path, etc.), combining base URLs
# with relative URLs, and encoding/decoding query strings.
import urllib.parse

def download_files(first_url, output_dir):  # first_url is the URL for the first item in the sequence
  if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

  # The first solution splits the URL using os.path.split, which treats the URL as a filesystem path string.
  url_head, url_tail = os.path.split(first_url)

  # The second solution parses the URL using urllib.parse.urlparse, which properly divides it into components (scheme, netloc, path).
  # url_head1, url_tail1 = urllib.parse.urlparse(first_url).netloc, urllib.parse.urlparse(first_url).path

  # Extracts all sequences of digits from the end-part (tail) of the URL, which is usually the filename.
  # The [-1] selects the last number found, assuming the filename includes an index or sequence number.
  # For example, for 'image_005.jpg', this would extract '005' as the first index.
  first_index = re.findall(r'[0-9]+', url_tail)[-1]

  index_count, error_count = 0, 0

  while error_count < 5:
    next_index = str(int(first_index) + index_count)
    
    # This block checks if the sequence number in the original filename starts with a '0' (meaning it is zero-padded).
    # If so, it pads the calculated next_index with leading zeros to match the original length,
    # so that generated filenames like 'image_005.jpg', 'image_006.jpg' have consistent padding.
    if first_index[0] == '0':
      next_index = '0' * (len(first_index) - len(next_index)) + next_index

    # This line constructs the URL for the next file to download in the sequence.
    # - re.sub(first_index, next_index, url_tail) replaces the current index in the filename with the next index.
    #   For example, if url_tail is 'image_005.jpg', first_index is '005', and next_index is '006',
    #   the result will be 'image_006.jpg'.
    # - urllib.parse.urljoin(url_head, ...) combines the head (base path) of the URL with the new filename.
    #   This ensures a valid URL like 'http://example.com/images/image_006.jpg'.
    next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))
    
    try:
      # Construct the path where the downloaded file will be saved locally.
      # - re.sub(first_index, next_index, url_tail) generates the expected filename for this step in the sequence
      #   (for example, changing 'image_005.jpg' to 'image_006.jpg').
      # - os.path.join(output_dir, ...) builds the full path so the file is saved in the requested output directory.
      output_file = os.path.join(output_dir, re.sub(first_index, next_index, url_tail))

      # Download the file from the constructed URL and save it to output_file.
      # urllib.request.urlretrieve(next_url, output_file) downloads the file at next_url
      # and writes it to the specified output_file on disk.
      urllib.request.urlretrieve(next_url, output_file)

      # Print a success message showing which file was downloaded (just the filename, not the whole path).
      # os.path.basename(next_url) extracts the final segment (the filename) from the URL.
      print(f'Successfully downloaded {os.path.basename(next_url)}')
    except:
      print(f'Could not retrieve {next_url}')
      error_count += 1
    index_count += 1

download_files('http://699340.youcanlearnit.net/image001.jpg', 'images')
