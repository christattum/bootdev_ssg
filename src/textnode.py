from enum import Enum

class TextType(Enum):
    TEXT_PLAIN = 1,
    TEXT_BOLD = 2,
    TEXT_ITALIC = 3,
    TEXT_CODE = 4,
    TEXT_LINK = 5,
    TEXT_IMAGE = 6

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
