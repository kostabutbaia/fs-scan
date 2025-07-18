import stat
from collections import defaultdict

from .file import File
from .class_info import ClassInfo

class PermsInfo:
    """ Class that defines information about permissions of files """
    def __init__(self):
        self._grouped_files = defaultdict(ClassInfo)

    def add(self, file: File) -> None:
        # A file can have multiple descriptions for unusual permissions.
        # For example, '---------' falls under both "no permissions" and "owner has no access".
        for unusual_perm in unusual_perms:
            if unusual_perm.check(file.permissions):
                self._grouped_files[unusual_perm.name()].add(file)

    @property
    def to_dict(self) -> dict:
        return self._grouped_files

class WorldWritable:
    def name() -> str:
        return "world-writable"

    def check(file_perms: int) -> bool:
        return bool(file_perms & stat.S_IWOTH)

class NoPermissions:
    def name() -> str:
        return "no-permissions"

    def check(file_perms: int) -> bool:
        return (
            file_perms & stat.S_IRWXU == 0 and
            file_perms & stat.S_IRWXG == 0 and
            file_perms & stat.S_IRWXO == 0
        )
    
class OwnerNoAccess:
    def name() -> str:
        return "owner-no-access"

    def check(file_perms: int) -> bool:
        owner_perms = stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR
        return (file_perms & owner_perms) == 0

unusual_perms = [
    WorldWritable,
    NoPermissions,
    OwnerNoAccess
]


# no permissions
# owner has no access
# world-readable only
# world-writable
# world-executable only
# fully world-writable
# execute-only (no read/write)
# setuid
# setgid
# sticky bit set
# full open access (rwxrwxrwx)
# setuid without execute
# setgid without execute
# owner write-only
# group write-only
# owner no execute
# group no execute