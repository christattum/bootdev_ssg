import unittest
from generate_pages import extract_title

class TestGeneratePages(unittest.TestCase):
    def test_extract_title_pulls_heading_1(self):
        md = "Here is some text\n\n# This is my title\n\nHere is a paragraph"
        title = extract_title(md)
        self.assertEqual("This is my title", title)

    def test_extract_title_throws_exception_if_heading_malformed(self):
        md = "Here is some text\n\n#This is my title\n\nHere is a paragraph"
        with self.assertRaises(RuntimeError):
            title = extract_title(md)

    def test_extract_title_throws_exception_if_heading_missin(self):
        md = "Here is some text\n\nAnother paragraph\n\n## A heading 2\n\n\Here is a paragraph"
        with self.assertRaises(RuntimeError):
            title = extract_title(md)
