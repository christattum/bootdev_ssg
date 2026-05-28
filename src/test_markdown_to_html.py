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
            '<div><h1>Tolkien Fan Club</h1><p><img src="/images/tolkien.png" alt="JRR Tolkien sitting"></img></p></div>'
        )

    def test_paragraph_with_bold_text(self):
        md = "Text with **bold** text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>Text with <b>bold</b> text</p></div>',
        )

    def test_paragraph_with_multiple_bold_text(self):
        md = "Text with **bold** text and **more bold** text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>Text with <b>bold</b> text and <b>more bold</b> text</p></div>',
        )

    def test_paragraph_with_italic_text(self):
        md = "Text with _italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>Text with <i>italic</i> text</p></div>',
        )

    def test_paragraph_with_multiple_italic_text(self):
        md = "Text with _italic_ text and _more italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>Text with <i>italic</i> text and <i>more italic</i> text</p></div>',
        )

    def test_heading_with_bold_text(self):
        md = "# Heading with **bold** text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Heading with <b>bold</b> text</h1></div>',
        )

    def test_heading_with_multiple_bold_text(self):
        md = "# Heading with **bold** text and **more bold** text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Heading with <b>bold</b> text and <b>more bold</b> text</h1></div>',
        )

    def test_heading_with_italic_text(self):
        md = "# Heading with _italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Heading with <i>italic</i> text</h1></div>',
        )

    def test_heading_with_multiple_italic_text(self):
        md = "# Heading with _italic_ text and _more italic_ text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h1>Heading with <i>italic</i> text and <i>more italic</i> text</h1></div>',
        )


    def test_quote(self):
        md = """
> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>"I am in fact a Hobbit in all but size."\n\n-- J.R.R. Tolkien</blockquote></div>',
        )

    def test_ordered_list(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>',
        )

    def test_ordered_test_with_bold_italic(self):
        md = """
1. Item 1 with **bold** text
2. Item 2 with _italic_ text
3. Item 3 with **bold** and _italic_ text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>Item 1 with <b>bold</b> text</li><li>Item 2 with <i>italic</i> text</li><li>Item 3 with <b>bold</b> and <i>italic</i> text</li></ol></div>'
        )

    def test_ordered_list_with_links(self):
        md = """
1. Item 1 with a [link](http://example.com/item1)
2. Item 2 with a [link](http://example.com/item2)
3. Item 3 with a [link](http://example.com/item3)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>Item 1 with a <a href="http://example.com/item1">link</a></li><li>Item 2 with a <a href="http://example.com/item2">link</a></li><li>Item 3 with a <a href="http://example.com/item3">link</a></li></ol></div>',
        )


    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>',
        )

    def test_unordered_list_containing_hyphens(self):
        md = """
- Item - 1
- Item - 2
- Item - 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>Item - 1</li><li>Item - 2</li><li>Item - 3</li></ul></div>',
        )

    def test_unordered_test_with_bold_italic(self):
        md = """
- Item 1 with **bold** text
- Item 2 with _italic_ text
- Item 3 with **bold** and _italic_ text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>Item 1 with <b>bold</b> text</li><li>Item 2 with <i>italic</i> text</li><li>Item 3 with <b>bold</b> and <i>italic</i> text</li></ul></div>'
        )

    def test_unordered_list_with_links(self):
        md = """
- Item 1 with a [link](http://example.com/item1)
- Item 2 with a [link](http://example.com/item2)
- Item 3 with a [link](http://example.com/item3)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>Item 1 with a <a href="http://example.com/item1">link</a></li><li>Item 2 with a <a href="http://example.com/item2">link</a></li><li>Item 3 with a <a href="http://example.com/item3">link</a></li></ul></div>',
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