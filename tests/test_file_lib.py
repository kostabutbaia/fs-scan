import unittest
import shutil
import os

from FileLib.file_library import FileLibrary
from FileLib.class_info import File

from utils import TempFile, create_file_system, class_info

TEST_BASE_DIR = './tests'
TEST_DIR = 'test_dir'

TEST_DIR_PATH = os.path.join(TEST_BASE_DIR, TEST_DIR)

class TestFileLibrary(unittest.TestCase):
    """ 
    Unit tests for scan options in the FileLibrary
    """

    def tearDown(self):
        """ Remove test directory after each test. """
        shutil.rmtree(TEST_DIR_PATH, ignore_errors=True)

    def test_scan_groups_simple(self):
        """ Test flat directory structure """
        simple_case = {
            TEST_DIR: {
                'file1': TempFile('file1', '.exe', 10),
                'file2': TempFile('file2', '.jpg', 10)
            }
        }
        create_file_system(TEST_BASE_DIR, simple_case)
        file_lib = FileLibrary(TEST_DIR_PATH, True, False)
        file_lib.scan_dirs()

        expected = {
                    'application': class_info(
                        1,
                        10,
                        [File('file1.exe', os.path.join(TEST_DIR_PATH, 'file1.exe'))]
                    ),
                    'image': class_info(
                        1,
                        10,
                        [File('file2.jpg', os.path.join(TEST_DIR_PATH, 'file2.jpg'))]
                    )
                }

        self.assertEqual(expected, file_lib.get_grouped_files())

    def test_scan_groups_nested(self):
        """ Test nested directory structure """
        simple_case = {
            TEST_DIR: {
                'file1': TempFile('file1', '.exe', 10),
                'dir_2': {
                    'file2': TempFile('file2', '.jpg', 10)
                }
            }
        }
        create_file_system(TEST_BASE_DIR, simple_case)
        file_lib = FileLibrary(TEST_DIR_PATH, True, False)
        file_lib.scan_dirs()

        expected = {
                    'application': class_info(
                        1,
                        10,
                        [File('file1.exe', os.path.join(TEST_DIR_PATH, 'file1.exe'))]
                    ),
                    'image': class_info(
                        1,
                        10,
                        [File('file2.jpg', os.path.join(TEST_DIR_PATH, 'dir_2', 'file2.jpg'))]
                    )
                }

        self.assertEqual(expected, file_lib.get_grouped_files())