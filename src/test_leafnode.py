import unittest
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')