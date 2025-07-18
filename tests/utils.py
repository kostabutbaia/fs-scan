import os

from FileLib.class_info import ClassInfo
from FileLib.file import File

class TempFile:
    """ 
    Represents a temporary file with a given name, extension, and size.
    
    Use the `create_file` method to generate a file with the specified size
    at the given path.
    """
    def __init__(self, name: str, ext: str, size: int):
        self.size = size
        self.name = name
        self.ext = ext

    def create_file(self, path: str) -> None:
        full_path = os.path.join(path, self.name + self.ext)

        with open(full_path, 'wb') as f:
            f.truncate(self.size) 

def create_file_system(path: str, file_system: dict) -> None:
    """
    Recursively creates a file system structure from a nested dictionary.

    Args:
        path (str): The base directory where the structure will be created.
        file_system (dict): A nested dictionary where:
            - keys are directory or file names
            - values are either another dict (for directories) or TempFile instances (for files)
    """
    for item_name, item_content in file_system.items():
        if isinstance(item_content, TempFile):
            item_content.create_file(path)
        if isinstance(item_content, dict):
            path = os.path.join(path, item_name)
            os.makedirs(path, exist_ok=True)
            create_file_system(path, file_system[item_name])

def class_info(total_files: int, total_size: int, files: list[File]) -> ClassInfo:
    """ 
    Constructs and returns a ClassInfo object with the provided metadata, for testing.
    """
    class_info = ClassInfo()
    class_info._files = files
    class_info._total_files = total_files
    class_info._total_size = total_size

    return class_info

def filemode_to_int(mode_str: str) -> int:
    """
    Convert a string of permissions (like '-rw-r--r--') to an octal int (like 0o644).
    """
    if len(mode_str) != 10:
        raise ValueError("Expected 10-character string like")
    
    perms = mode_str[1:]
    mode = 0

    for i, ch in enumerate(perms):
        shift = 3 * (2 - i // 3)
        if ch == 'r':
            mode |= 0b100 << shift
        elif ch == 'w':
            mode |= 0b010 << shift
        elif ch == 'x':
            mode |= 0b001 << shift

    return mode