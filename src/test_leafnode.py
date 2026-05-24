import unittest
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)

    def test_to_html(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), f'<a href="https://www.google.com">Click Me!</a>')