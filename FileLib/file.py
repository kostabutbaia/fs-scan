import os
import stat
import mimetypes

from .utils import format_size

class File:
    """ Class that defines metadata about a file """
    def __init__(self, file_name: str, path: str):
        self.path = os.path.abspath(path) # If relative path, Then change into absolute path
        self.file_name = file_name
        self.file_size = os.path.getsize(self.path)
        self.permissions = os.stat(self.path).st_mode

        mime_type, _ = mimetypes.guess_type(self.file_name)
        if mime_type != None:
            self.file_category = mime_type.split('/')[0]
        else:
            self.file_category = 'other'
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, File):
            return False

        return (
            self.file_name == other.file_name and
            self.file_size == other.file_size and
            self.permissions == other.permissions and
            self.file_category == other.file_category
        )
    
    @property
    def to_dict(self) -> dict:
        return {
            'file_name': self.file_name,
            'path': self.path,
            'file_size': format_size(self.file_size),
            'permissions': stat.filemode(self.permissions)
        }