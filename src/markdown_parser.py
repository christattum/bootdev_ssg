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

        split_text = old_node.text.split(delimiter)
        if len(split_text) >= 3 and len(split_text) % 2 == 1:    
           # should be an odd number if delimiters are matched
           for i in range(0, len(split_text)):
                # odd lines are bold/italic etc., even numbers are plain
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_text[i], TextType.PLAIN))     
                else:
                    new_nodes.append(TextNode(split_text[i], text_type))     
                
        elif len(split_text) % 2 == 0:
            raise ValueError('unmatched delimiters')
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

def markdown_to_blocks_crap(markdown: str):
    blocks = markdown.strip().split("\n\n")
    stripped_blocks = list(filter(lambda x: len(x) != 0, map(lambda x: x.strip(), blocks)))
    return stripped_blocks

def markdown_to_blocks(markdown: str):
    blocks = []
    lines = markdown.strip().split("\n")

    current_block = []

    in_code_block = False
    for line in lines:
        # If this line is a code fence, add it and toggle code state.
        if line.startswith("```"):
            current_block.append(line)
            in_code_block = not in_code_block

        # If this line is blank and we're not in code, finish the current block.
        # Making sure to only add a block if it has anything in it
        elif line == '' and not in_code_block:
            if len(current_block) > 0:
                block_text = "\n".join(current_block)
                blocks.append(block_text)
                current_block = []

        # Otherwise, add this line to the current block.
        else:
            current_block.append(line)

    # Append any left over block
    if len(current_block) > 0:
        block_text = "\n".join(current_block)
        blocks.append(block_text)

    return blocks
    
def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.PLAIN)

    nodes = [initial_node]
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.+?)\]\((.+?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.+?)\]\((.+?)\)", text)
    return matches

