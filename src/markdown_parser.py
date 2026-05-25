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

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        # Only split PLAIN text nodes, otherwise pass through as is
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        images = extract_markdown_images(text)
        for image in images:
            image_text = f"![{image[0]}]({image[1]})"

            # Break off first part of string before image, then image and rest of string part
            split_text = text.split(image_text)

            # Add first part as TextNode
            new_nodes.append(TextNode(split_text[0], TextType.PLAIN))

            # Then add the image
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            # Set text to remaining part, before looping around for next image
            text = split_text[1]

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        # Only split PLAIN text nodes, otherwise pass through as is
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        links = extract_markdown_links(text)
        for link in links:
            link_text = f"[{link[0]}]({link[1]})"

            # Break off first part of string before link, then link and rest of string part
            split_text = text.split(link_text)

            # Add first part as TextNode
            new_nodes.append(TextNode(split_text[0], TextType.PLAIN))

            # Then add the link
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            
            # Set text to remaining part, before looping around for next link
            text = split_text[1]

        return new_nodes
    
def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.PLAIN)
    nodes = [initial_node]

    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_link(nodes)
    return nodes

    nodes = split_nodes_image(nodes)

    return nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.+?)\]\((.+?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.+?)\]\((.+?)\)", text)
    return matches

