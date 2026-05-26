import unittest
from textnode import TextNode, TextType
from markdown_parser import split_nodes_link

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