import unittest
from textnode import TextNode, TextType
from markdown_parser import text_to_textnodes

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