import unittest
from textnode import TextNode, TextType
from markdown_parser import split_nodes_image

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