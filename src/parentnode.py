from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.children is None:
            raise ValueError("Parent nodes must have children")
        
        result = ""
        for node in self.children:
            result += node.to_html()

        if self.props is None:
            return f"<{self.tag}>{result}</{self.tag}>"
        
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"

