import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "My paragraph text", 
                        [HTMLNode("p", "Child paragraph")], 
                        {"prop1": "value1", "prop2:": "value2"})
        node2 = HTMLNode("p", "My paragraph text", 
                         [HTMLNode("p", "Child paragraph")], 
                         {"prop1": "value1", "prop2:": "value2"})
        self.assertEqual(node, node2)