from markdown_parser import markdown_to_blocks

def extract_title(markdown):

    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            title = block.replace("# ", "")
            return title

    raise RuntimeError('Missing Title')