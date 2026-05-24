import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_plain(self):
        node = TextNode("This is plain text", TextType.PLAIN)
        self.assertEqual(repr(node), f"TextNode(This is plain text, TextType.PLAIN, None)")
        
    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        self.assertEqual(repr(node), f"TextNode(This is bold text, TextType.BOLD, None)")

if __name__ == "__main__":
    unittest.main()