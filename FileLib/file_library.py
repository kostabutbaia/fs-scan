import os
from collections import defaultdict

from .file import File
from .class_info import ClassInfo
from .perms_info import PermsInfo

class FileLibrary:
    """ 
    Scans a directory tree and gathers metadata on all contained files

    Depending on initialization flags, this class can:
    - Group files by category (image, application, etc.)
    - Identify files with world-writable permission settings
    - Record files that exceed a given size threshold.

    """
    def __init__(self, dir_path: str, scan_groups: bool, scan_perms: bool, scan_size_threshold: int = 0):
        self.dir_path = os.path.abspath(dir_path) # If relative path, Then change into absolute path
        self.scan_groups = scan_groups
        self.scan_perms = scan_perms
        self.size_threshold = scan_size_threshold

        if scan_groups:
            self._grouped_files = defaultdict(ClassInfo)
        if scan_perms:
            self._perm_files = PermsInfo()
        if scan_size_threshold != 0:
            self._large_files = list()

    def get_grouped_files(self) -> dict:
        if self.scan_groups:
            return self._grouped_files
        raise RuntimeError("Grouped files were not scanned. Set scan_groups=True before scanning.")
    
    def get_large_files(self) -> list:
        if self.size_threshold != 0:
            return self._large_files
        raise RuntimeError("Large files were not scanned. Set scan_perms=True before scanning.")
    
    def get_perm_files(self) -> dict:
        if self.scan_perms:
            return self._perm_files
        raise RuntimeError("Permission files were not scanned. Set scan_size_threshold before scanning.")

    def scan_dirs(self) -> None:
        self._scan_dirs(self.dir_path)

    def _scan_dirs(self, dir_path: str) -> None:
        entries = os.listdir(dir_path)

        for item_name in entries:
            file_path = os.path.join(dir_path, item_name)
            
            if os.path.isfile(file_path):
                f = File(item_name, file_path)

                if self.scan_perms: # Store files with unusual perms
                    self._perm_files.add(f)

                if self.scan_groups: # Store files by category
                    self._grouped_files[f.file_category].add(f)

                if f.file_size > self.size_threshold and self.size_threshold != 0: # Store files if their size is larger than threshold
                    self._large_files.append(f)

            if os.path.isdir(file_path):
                self._scan_dirs(file_path)