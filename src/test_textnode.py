import unittest
from textnode import text_node_to_html_node, TextNode, TextType

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

    def test_link_with_url(self):
        node = TextNode("This is a link", TextType.LINK, "http://example.com")
        self.assertEqual(repr(node), f"TextNode(This is a link, TextType.LINK, http://example.com)")

    def test_url_defaults_to_none(self):
        node = TextNode("Link without a url", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_plain(self):
        node = TextNode("This is a plain text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a plain text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")  

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node") 

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a code text node") 

    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props["href"], "https://www.google.com")

    def test_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "https://www.google.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props["src"], "https://www.google.com")    
        self.assertEqual(html_node.props["alt"], "This is an image text node")    


if __name__ == "__main__":
    unittest.main()