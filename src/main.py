from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", 
                    TextType.TEXT_LINK, 
                    "https://christattum.com")
    print(node)

main()