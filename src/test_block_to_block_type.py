import unittest
from blocktype import BlockType
from block_to_block_type import block_to_block_type

class TestBlockTypes(unittest.TestCase):
    
    def test_paragraph_block(self):
        block = "Here is some paragraph text"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_valid_heading_1_block(self):
        block = "# This is a heading 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_heading_without_space_is_paragraph_block(self):
        block = "#This is not a heading 1"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_valid_code_block(self):
        block = """```
This is first line
This is second line
```
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_valid_quote_block(self):
        block = """> This is quote line 1
>This is quote line 2
> This is quote line 2
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_block_without_all_correct_leading_symbol_is_paragraph(self):
        block = """> This is quote line 1
> This is quote line 2
This is quote line 2
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_valid_unordered_list_block(self):
        block = """- This is first item
- This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_without_space_is_paragraph_block(self):
        block = """- This is first item
-This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_valid_ordered_list_block(self):
        block = """1. This is first item
2. This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_ordered_list_without_spaces_is_paragraph(self):
        block = """1. This is first item
2.This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_without_fullstop_is_paragraph(self):
        block = """1. This is first item
2 This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_with_out_of_order_numbers_is_paragraph(self):
        block = """2. This is first item
1. This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)