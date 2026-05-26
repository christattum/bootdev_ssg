import unittest
from copy_files import copy_files

class TestCopyFiles(unittest.TestCase):

    def setUp(self):
        self.log = []

    def logger(self, text: str):
        self.log.append(text)

    def test_copy_files(self):
        copy_files("./static", "./public", self.logger)
        self.assertListEqual([
            "Running in test mode"
        ], self.log)