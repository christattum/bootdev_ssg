from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        split_text = old_node.text.split(delimiter)
        for text in split_text:
            new_node = TextNode(text, TextType.PLAIN)
            new_nodes.append(new_node)

    return new_nodes

