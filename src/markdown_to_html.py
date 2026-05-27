from parentnode import ParentNode
from leafnode import LeafNode
from blocktype import BlockType
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_parser import markdown_to_blocks, split_nodes_delimiter, text_to_textnodes
from block_to_block_type import block_to_block_type, get_heading_level

def create_heading_node(block: str, level: int):
    block = block.replace("#" * level + " ", "")
    node = LeafNode(f"h{level}", block)
    return node

def create_blockquote_node(block: str):
    # Remove > 
    block = block.replace("> ", "")
    block = block.replace(">", "")

    node = LeafNode("blockquote", block)
    return node

def create_unordered_list_node(block: str):
    li_nodes = []
    items = block.split("\n")
    for item in items:
        item = item.replace("- ", "")
        text_nodes = text_to_textnodes(item)
        children = []
        for text_node in text_nodes:
            leaf_node = text_node_to_html_node(text_node)
            children.append(leaf_node)

        li_node = ParentNode("li", children)
        li_nodes.append(li_node)

    node = ParentNode("ul", li_nodes)
    return node

def create_ordered_list_node(block: str):
    pass

def create_paragraph_node(block: str):
    text_nodes = text_to_textnodes(block)
    children = []
    for text_node in text_nodes:
        node = text_node_to_html_node(text_node)

        # replace any newlines with spaces
        node.value = node.value.replace("\n", " ")

        children.append(node)

    node = ParentNode("p", children)
    return node

def create_code_node(block: str):
    # strip any leading or trailing lines (above and below ```)
    block = block.strip()

    # remove opening ``` and the new line after it
    content_text = block.replace("```\n", "")

    # remove closing ``` but leave any new lines above it
    content_text = content_text.replace("```", "")

    # Code block is treated as raw, any **, _ etc are ignored
    text_node =  TextNode(content_text, TextType.CODE)
    code_node = text_node_to_html_node(text_node)
    pre_node = ParentNode("pre", [code_node])

    return pre_node


def markdown_to_html_node(markdown: str):

    children = []

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        node = None
        if block_type == BlockType.PARAGRAPH:
            node = create_paragraph_node(block)
        elif block_type == BlockType.CODE:
            node = create_code_node(block)
        elif block_type == BlockType.QUOTE:
            node = create_blockquote_node(block)
        elif block_type == BlockType.HEADING:
            level = get_heading_level(block)
            node = create_heading_node(block, level)
        elif block_type == BlockType.ORDERED_LIST:
            node = create_ordered_list_node(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = create_unordered_list_node(block)

        if node is not None:
            children.append(node)

    parent_node = ParentNode("div", children)

    return parent_node