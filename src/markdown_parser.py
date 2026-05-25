from textnode import TextNode, TextType
from blocktype import BlockType
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

        # if no images are found, then pass the node through
        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            image_text = f"![{image[0]}]({image[1]})"

            # Break off first part of string before image, then image and rest of string part
            split_text = text.split(image_text)

            # Add first part as TextNode if there is any text before the image
            if len(split_text[0]) != 0:
                new_nodes.append(TextNode(split_text[0], TextType.PLAIN))

            # Then add the image
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            # Set text to remaining part, before looping around for next image
            text = split_text[1]

        # append any remaining text
        if len(text) != 0:
            new_nodes.append(TextNode(text, TextType.PLAIN))

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

        # if no links are found, then pass the node through
        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            link_text = f"[{link[0]}]({link[1]})"

            # Break off first part of string before link, then link and rest of string part
            split_text = text.split(link_text, maxsplit=1)

            # Add first part as TextNode if there is any text before the link
            if len(split_text[0]) != 0:
                new_nodes.append(TextNode(split_text[0], TextType.PLAIN))

            # Then add the link
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            
            # Set text to remaining part, before looping around for next link
            text = split_text[1]

        # append any remaining text
        if len(text) != 0:
            new_nodes.append(TextNode(text, TextType.PLAIN))

    return new_nodes

def markdown_to_blocks(markdown: str):
    blocks = markdown.strip().split("\n\n")
    stripped_blocks = list(filter(lambda x: len(x) != 0, map(lambda x: x.strip(), blocks)))
    return stripped_blocks
    
def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.PLAIN)

    nodes = [initial_node]
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def is_ul_block(block):
    lines = block.split("\n")
    for line in lines:
        if len(line) >= 2:
            if line[0] != '-' or line[1] != ' ':
                return False
    
    return True

def is_ol_block(block):
    lines = block.split("\n")
    line_no = 1
    for line in lines:
        if len(line) <= 2:
            return False
        # TODO: use regex here, line number can be any number of digits
        if ord(line[0]) != line_no or line[1] != '.':
            return False
        line_no += 1

    return True

def is_quote_block(block):
    lines = block.split("\n")
    for line in lines:
        if len(line) <= 1:
            return False
        if line[0] != '<':
            return False
    
    return True

def is_code_block(block):
    lines = block.split("\n")
    print("code", lines)
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return True
    
    return False

def block_to_block_type(block):
    if len(block) <= 2:
        return BlockType.PARAGRAPH
        
    if block.startswith('-') and is_ul_block(block):
        return BlockType.UNORDERED_LIST
    
    if block.startswith('1') and is_ol_block(block):
        return BlockType.ORDERED_LIST
    
    if block.startswith('<') and is_quote_block(block):
        return BlockType.QUOTE

    if block.startswith('# '):
        return BlockType.HEADING
    
    if is_code_block(block):
        return BlockType.CODE
    
    return BlockType.PARAGRAPH

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.+?)\]\((.+?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.+?)\]\((.+?)\)", text)
    return matches

