import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "My paragraph text")
        node2 = HTMLNode("p", "My paragraph text")
        self.assertEqual(node, node2)