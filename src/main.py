from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("This is some anchor text", 
                    TextType.LINK, 
                    "https://christattum.com")
    print(node)

    node = HTMLNode("p", "My paragraph text", 
                        [HTMLNode("p", "Child paragraph")], 
                        {"prop1": "value1", "prop2": "value2"})
    print(node)
    print("[" + node.props_to_html() + "]")

if __name__ == "__main__":
    main()