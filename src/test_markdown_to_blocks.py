import unittest
from markdown_parser import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_empty_blocks_are_removed(self):
        md = """



This is the first actual block



This is the second actual block




- This is the third block
- With another item



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "This is the first actual block",
            "This is the second actual block",
            "- This is the third block\n- With another item"
        ])

    def test_given_example(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
                [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
