from .file import File
from .utils import format_size

class ClassInfo:
    """ Class that defines information about a group of files """
    def __init__(self):
        self._total_files = 0
        self._total_size = 0
        self._files = list()

    def add(self, file: File) -> None:
        self._total_files += 1
        self._total_size += file.file_size
        self._files.append(file)

    def __eq__(self, other) -> bool:
        if not isinstance(other, ClassInfo):
            return False

        return (
            self._total_files == other._total_files and
            self._total_size == other._total_size and
            self._files == other._files
        )

    @property
    def to_dict(self) -> dict:
        return {
            'total_files': self._total_files,
            'total_size': format_size(self._total_size),
            'files': self._files
        }