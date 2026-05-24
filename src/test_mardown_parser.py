import unittest
from textnode import TextNode, TextType
from markdown_parser import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_node(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        # [
        #     TextNode("This is text with a ", TextType.TEXT),
        #     TextNode("code block", TextType.CODE),
        #     TextNode(" word", TextType.TEXT),
        # ]   

        self.assertEqual(len(new_nodes), 3)
        self.assertIsInstance(new_nodes[0], TextNode)
        self.assertIsInstance(new_nodes[1], TextNode)
        self.assertIsInstance(new_nodes[2], TextNode)
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)
        self.assertEqual(new_nodes[2].text, " word")
