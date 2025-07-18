import json
import os

from FileLib.file_library import FileLibrary
from .utils import object_json_serializer, flatten_path

class FileWriterJSON:
    def __init__(self, file_lib: FileLibrary, output_path: str):
        self.file_lib = file_lib
        self.output_path = os.path.abspath(output_path) # If relative path, Then change into absolute path

    def generate_reports(self) -> None:
        if self.file_lib.scan_groups:
            self.generate_class_report()
        if self.file_lib.size_threshold != 0:
            self.generate_large_report()
        if self.file_lib.scan_perms:
            self.generate_perm_report()

    def generate_class_report(self) -> None:
        grouped_files = self.file_lib.get_grouped_files()
        full_path = os.path.join(self.output_path, f'class_report_{flatten_path(self.file_lib.dir_path)}.json')

        with open(full_path, 'w') as f:
            json.dump(grouped_files, f, default=object_json_serializer, indent=2)
    
    def generate_large_report(self) -> None:
        large_files = self.file_lib.get_large_files()
        full_path = os.path.join(self.output_path, f'large_report_{flatten_path(self.file_lib.dir_path)}.json')

        with open(full_path, 'w') as f:
            json.dump(large_files, f, default=object_json_serializer, indent=2)
    
    def generate_perm_report(self) -> None:
        perm_files = self.file_lib.get_perm_files()
        full_path = os.path.join(self.output_path, f'perm_report_{flatten_path(self.file_lib.dir_path)}.json')

        with open(full_path, 'w') as f:
            json.dump(perm_files, f, default=object_json_serializer, indent=2)