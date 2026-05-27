import unittest
from markdown_parser import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_first_part_tolkien(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, 
            [
                "# Tolkien Fan Club",
                "![JRR Tolkien sitting](/images/tolkien.png)",
                "Here's the deal, **I like Tolkien**."
            ])


    def test_lines_between_paragraphs_are_stripped(self):
        md =  "para one\n\n\npara two"
        # should produce two paragraph-ish blocks, with no empty block
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, 
            [
                "para one",
                "para two"
            ])


    def test_lines_inside_code_blocks_are_preserved(self):
        md = "```\nline one\n\nline three\n```"
        # should stay one code block, including the blank line
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "```\nline one\n\nline three\n```"

        ])

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
