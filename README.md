# File System Analyzer

A Python tool to scan, analyze and group all the files under a directory by their type, size and permission attributes. Useful detecting unusual file permissions and generating summaries of directory contents.

## Setup
Python is required to run this tool, to see help on usage you can run:
```
python main.py --help
```
## Generating Reports
This Python tool generates report files for the specified `dir` and saves them to `out_path`. It supports the following types of reports:
- Grouped by file type (images, videos, applications)
- Files with unusual permissions (world-writable, no permissions)
- Files exceeding a size threshold (in bytes)

User can specify which reports to generate by specifying their respective flags in the command:
```
python main.py <dir> <out_path> [--groups] [--perms] [--size SIZE]
```
Below are examples of what the output will look like for each type of report.
### Group by type
This report tool groups files of similar extension types according to Python `mimetypes`: application, audio, image, video and text. if not recognized then it is categorized under `other`
#### Example
If directory tree for `dir` looks like the following: 
```text
dir/
├─ file1.exe
├─ dir_2/
│  ├─ file2.jpg
```
Then running `python main.py <dir> <out_path> --groups` will generate the following JSON file in `out_path` directory:
```json
{
  "image": {
    "total_files": 1,
    "total_size": "10.00 B",
    "files": [
      {
        "file_name": "file2.jpg",
        "path": "dir_2\\file2.jpg",
        "file_size": "10.00 B",
        "permissions": "-rw-rw-rw-"
      }
    ]
  },
  "application": {
    "total_files": 1,
    "total_size": "10.00 B",
    "files": [
      {
        "file_name": "file1.exe",
        "path": "file1.exe",
        "file_size": "10.00 B",
        "permissions": "-rwxrwxrwx"
      }
    ]
  }
}
```

### Group by unusual permissions
This report tool groups files of similar unusual permission type for the specified `dir` and saves them to `out_path`. Can be used by using it's flag `--perms` in the command. This tool checks for following unusual types:

- **World-Writable Permission**  
  The file can be modified by anyone. \
  _Permission pattern:_ `___ ___ _w_`, _Example:_ `---rw--w-`

- **Owner No Access Permission**  
  The file's owner has no read, write or execute permissions.\
  _Permission pattern:_ `--- ___ ___`, _Example:_ `---rw-r--`

- **No Permissions**  
  No one has any access to the file.\
  _Permission pattern:_ `--- --- ---`

The output JSON file will follow the same structure as above but will group files based on the these unusual permission patterns.

### Scan for Oversized Files
This report tool scans for files whose size exceeds the specified threshold and stores them in a JSON file. The threshold is set using the `--size` flag and the value should be provided in bytes.

```
python main.py /home/user/documents reports/output.json --size 1000000
```
Since `1000000 Mb ~ 1 MB` this command will scan for files with size greater than `1 MB`