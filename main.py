import argparse
import os

from FileWriter.file_writer import FileWriterJSON
from FileLib.file_library import FileLibrary

def main():
    args = parse_args()

    if not os.path.isdir(args.dir):
        raise RuntimeError(f'\'{args.dir}\' is not a valid directory.')
    
    if not os.path.isdir(args.out_path):
        raise RuntimeError(f'\'{args.out_path}\' is not a valid directory.')

    file_library = FileLibrary(
        dir_path=args.dir,
        scan_groups=args.groups,
        scan_perms=args.perms,
        scan_size_threshold=args.size
    )
    file_library.scan_dirs()

    file_writer = FileWriterJSON(file_library, args.out_path)

    file_writer.generate_reports()

def parse_args():
    parser = argparse.ArgumentParser(description="Scan a directory for file metadata.")
    parser.add_argument("dir", type=str, help="Directory path to scan")
    parser.add_argument("out_path", type=str, help="Path for storing reports")
    parser.add_argument("--groups", action="store_true", help="Generate report by grouping files by category")
    parser.add_argument("--perms", action="store_true", help="Generate report for files with unusual permissions")
    parser.add_argument("--size", type=int, default=0, help="Generate report of files whose size is greater than threshold")

    return parser.parse_args()


if __name__ == '__main__':
    main()