from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # Only split PLAIN text nodes, otherwise pass through as is
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        # maxsplit = 2, for opening and closing delimiter
        # which results in 3 strings
        split_text = old_node.text.split(delimiter, maxsplit=2)
        if len(split_text) == 3:
            new_nodes.append(TextNode(split_text[0], TextType.PLAIN))
            new_nodes.append(TextNode(split_text[1], text_type))
            new_nodes.append(TextNode(split_text[2], TextType.PLAIN))
        elif len(split_text) == 2:
            raise ValueError('missing')
        elif len(split_text) == 1:
            new_nodes.append(TextNode(split_text[0], TextType.PLAIN))
        else:
            raise RuntimeError('Unexpected error')

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.+?)\]\((.+?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.+?)\]\((.+?)\)", text)
    return matches

