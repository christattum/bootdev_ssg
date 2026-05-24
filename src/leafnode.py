from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if value is None:
            raise ValueError("value is required")
        
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Value is missing')
        
        # Return raw text if there is no tag
        if self.tag is None:
            return self.value
        
        if self.props is None:
            return f'<{self.tag}>{self.value}<{self.tag}>'
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

        
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

        

        
