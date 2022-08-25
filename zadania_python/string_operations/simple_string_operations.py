# Write class that will check word count in provided text file. Instantiate class with content of the file.
# Implement method that will return following result:
# Eg. 'Lorem': 1, 'ipsum': 2, 'dolor': 1, 'sit': 2, 'amet,': 1, ...

from pathlib import Path


if __name__ == "__main__":
    file_path = Path.cwd() / "lorem_ipsum.txt"

    pass
