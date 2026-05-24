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

    def test_repr(self):
        node = HTMLNode("p", "My paragraph text", 
                        [HTMLNode("p", "Child paragraph")], 
                        {"prop1": "value1", "prop2:": "value2"})
        self.assertEqual(repr(node),"HTMLNode(p, My paragraph text, [HTMLNode(p, Child paragraph, None, None)], {'prop1': 'value1', 'prop2:': 'value2'})")

    def test_props_to_html(self):
        node = HTMLNode("p", "My paragraph text", 
                        [HTMLNode("p", "Child paragraph")], 
                        {"prop1": "value1", "prop2": "value2"})
        
        html = node.props_to_html()
        self.assertEqual(html, " prop1=value1 prop2=value2")