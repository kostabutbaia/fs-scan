import unittest

from FileLib import perms_info

from utils import filemode_to_int

class TestPermissionChecks(unittest.TestCase):
    """ 
    Unit tests for checking unusual permissions
    """

    def test_world_writable(self):
        cases = [
            {'name': "case '----------'", 'case': filemode_to_int('----------'), 'expected': False},
            {'name': "case '-rw--w----'", 'case': filemode_to_int('-rw--w----'), 'expected': False},
            {'name': "case '--------w-'", 'case': filemode_to_int('--------w-'), 'expected': True},
            {'name': "case '--w--w--w-'", 'case': filemode_to_int('--w--w--w-'), 'expected': True},
            {'name': "case '-rw--w--w-'", 'case': filemode_to_int('-rw--w--w-'), 'expected': True},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], perms_info.WorldWritable.check(test_case['case']), msg=test_case['name'])

    def test_owner_no_access(self):
        cases = [
            {'name': "case '----------'", 'case': filemode_to_int('----------'), 'expected': True},
            {'name': "case '----r-----'", 'case': filemode_to_int('----r-----'), 'expected': True},
            {'name': "case '----r--w--'", 'case': filemode_to_int('----r--w--'), 'expected': True},
            {'name': "case '-rwx------'", 'case': filemode_to_int('-rwx------'), 'expected': False},
            {'name': "case '-r--------'", 'case': filemode_to_int('-r--------'), 'expected': False},
            {'name': "case '--w-------'", 'case': filemode_to_int('--w-------'), 'expected': False},
            {'name': "case '---x------'", 'case': filemode_to_int('---x------'), 'expected': False}
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], perms_info.OwnerNoAccess.check(test_case['case']), msg=test_case['name'])

    def test_no_permissions(self):
        cases = [
            {'name': "case '----------'", 'case': filemode_to_int('----------'), 'expected': True},
            {'name': "case '-r--------'", 'case': filemode_to_int('-r--------'), 'expected': False},
            {'name': "case '--w-------'", 'case': filemode_to_int('--w-------'), 'expected': False},
            {'name': "case '---x------'", 'case': filemode_to_int('---x------'), 'expected': False},
            {'name': "case '----r-----'", 'case': filemode_to_int('----r-----'), 'expected': False},
            {'name': "case '-----w----'", 'case': filemode_to_int('-----w----'), 'expected': False},
            {'name': "case '------x---'", 'case': filemode_to_int('------x---'), 'expected': False},
            {'name': "case '-------r--'", 'case': filemode_to_int('-------r--'), 'expected': False},
            {'name': "case '--------w-'", 'case': filemode_to_int('--------w-'), 'expected': False},
            {'name': "case '---------x'", 'case': filemode_to_int('---------x'), 'expected': False},
            {'name': "case '-rw-r--r--'", 'case': filemode_to_int('-rw-r--r--'), 'expected': False},
        ]

        for test_case in cases:
            self.assertEqual(test_case['expected'], perms_info.NoPermissions.check(test_case['case']), msg=test_case['name'])