import unittest
from textnode import TextNode, TextType
from blocktype import BlockType
from htmlnode import HTMLNode
from leafnode import LeafNode
from markdown_parser import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes, markdown_to_blocks, block_to_block_type

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_plain_text_node(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.PLAIN))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.PLAIN))

    def test_bold_text_node(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.PLAIN))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.PLAIN))

    def test_italic_text_node(self):
        node = TextNode("This is text with an _italic_ word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with an ", TextType.PLAIN))
        self.assertEqual(new_nodes[1], TextNode("italic", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.PLAIN))     

    def test_single_node_without_closing_delimiter_raises_exception(self):
        node = TextNode("This is text with a `code block without closing delimiter", TextType.PLAIN)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_italic_text_node_will_pass_through_as_new_node(self):
        node1 = TextNode("This is text with an _italic_ word", TextType.PLAIN)
        node2 = TextNode("This is bold text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node1, node2], "_", TextType.ITALIC)

        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0], TextNode("This is text with an ", TextType.PLAIN))
        self.assertEqual(new_nodes[1], TextNode("italic", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.PLAIN))
        self.assertEqual(new_nodes[3], TextNode("This is bold text", TextType.BOLD))

class TestExtractMarkdownLinks(unittest.TestCase):

    def test_given_example(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

class TestExtractMarkdownImages(unittest.TestCase):

    def test_given_example(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_single_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif")], matches)   

    def test_two_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

class TestSplitImages(unittest.TestCase):

    def test_given_example(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_should_pass_through_no_images(self):
        node = TextNode(
            "This is text with some **bold text** and some _italic text_ but no images",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with some **bold text** and some _italic text_ but no images", TextType.PLAIN),
            ],
            new_nodes,
        )

class TestSplitLinks(unittest.TestCase):

    def test_given_example(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.apple.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second link", TextType.LINK, "https://www.apple.com"
                ),
            ],
            new_nodes,
        )

    def test_should_pass_through_no_links(self):
        node = TextNode(
            "This is text with some **bold text** and some _italic text_ but no links",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with some **bold text** and some _italic text_ but no links", TextType.PLAIN),
            ],
            new_nodes,
        )

class TestTextToNodes(unittest.TestCase):

    def test_given_example(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    def test_with_a_link_and_image(self):
        text = "This is text with a [link](https://boot.dev) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            nodes
        )

    def test_with_a_link(self):
        text = "This is text with a [link](https://boot.dev)"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    def test_with_link_first_then_remaining_text(self):
        text = "[link](https://boot.dev) and some remaining text"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and some remaining text", TextType.PLAIN),
            ],
            nodes
        )

    def test_with_text_link_text(self):
        text = "This is text with a [link](https://boot.dev) and some remaining text"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and some remaining text", TextType.PLAIN),
            ],
            nodes
        )

    def test_with_image_first_then_remaining_text(self):
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and some remaining text"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and some remaining text", TextType.PLAIN),
            ],
            nodes
        )

    def test_with_text_image_text(self):
        text = "This is text with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and some remaining text"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and some remaining text", TextType.PLAIN),
            ],
            nodes
        )

    def test_with_an_image(self):
        text = "This is text with an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            nodes
        )

    def test_without_links_or_images(self):
        text = "This is **text** with an _italic_ word and a `code block` and no images or links"

        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" and no images or links", TextType.PLAIN),
            ],
            nodes
        )

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
        block = """
```
This is first line
This is second line
```
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_valid_quote_block(self):
        block = """
> This is quote line 1
>This is quote line 2
> This is quote line 2
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_quote_block_without_all_correct_leading_symbol_is_paragraph(self):
        block = """
> This is quote line 1
> This is quote line 2
This is quote line 2
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_valid_unordered_list_block(self):
        block = """
- This is first item
- This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_unordered_list_without_space_is_paragraph_block(self):
        block = """
- This is first item
-This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


    def test_valid_ordered_list_block(self):
        block = """
1. This is first item
2. This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)


    def test_ordered_list_without_spaces_is_paragraph(self):
        block = """
1. This is first item
2.This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_ordered_list_without_fullstop_is_paragraph(self):
        block = """
1. This is first item
2 This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


    def test_ordered_list_with_out_of_order_numbers_is_paragraph(self):
        block = """
2. This is first item
1. This is second item
"""
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)