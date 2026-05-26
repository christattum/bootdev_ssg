import unittest
from copy_files import copy_files, delete_files

class TestCopyFiles(unittest.TestCase):

    def setUp(self):
        self.log = []

    def logger(self, text: str):
        self.log.append(text)
        print(text)

    @unittest.skip("need to control which runs")
    def test_copy_files(self):
        copy_files("./static", "./public", self.logger, True)
        self.assertListEqual([
            "Running in test mode",
            "Copying /Users/chris/Workspace/Personal/boot.dev/bootdev_ssg/static/images/tolkien.png to /Users/chris/Workspace/Personal/boot.dev/bootdev_ssg/public/images/tolkien.png",
            "Copying /Users/chris/Workspace/Personal/boot.dev/bootdev_ssg/static/index.css to /Users/chris/Workspace/Personal/boot.dev/bootdev_ssg/public/index.css"
        ], self.log)

    @unittest.skip("need to control which runs")
    def test_delete_files(self):
        delete_files("./public", self.logger, True)
        self.assertListEqual([
            "Running in test mode",
            "Removing files from /Users/chris/Workspace/Personal/boot.dev/bootdev_ssg/public",
        ], self.log)