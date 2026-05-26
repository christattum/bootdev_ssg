from parentnode import ParentNode
from blocktype import BlockType
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_parser import markdown_to_blocks, split_nodes_delimiter, text_to_textnodes
from block_to_block_type import block_to_block_type

def create_paragraph_node(block):
    text_nodes = text_to_textnodes(block)
    children = []
    for text_node in text_nodes:
        node = text_node_to_html_node(text_node)
        children.append(node)

    node = ParentNode("p", children)
    return node

def create_code_node(block):
    node = ParentNode("pre", 
        [
            TextNode(block, TextType.CODE)
        ]
    )
    return node

def markdown_to_html_node(markdown):

    children = []

    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        node = None
        if block_type == BlockType.PARAGRAPH:
            node = create_paragraph_node(block)
        elif block_type == BlockType.CODE:
            node = create_code_node(block)

        if node is not None:
            children.append(node)

    parent_node = ParentNode("div", children)

    return parent_node