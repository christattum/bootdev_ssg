import unittest
from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):

    def test_tolkien_top(self):
        md = """
# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Tolkien Fan Club</h1><p><img src="/tolkienfanclub/images/tolkienprofile.png" alt="JRR Tolien sitting"></img></p></div>'
        )


    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_codeblock_with_opening_new_lines(self):
        md = """
```



This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\n\n\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_codeblock_with_closing_new_lines(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff



```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n\n\n\n</code></pre></div>",
        )