from markdown_parser import markdown_to_blocks
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            title = block.replace("# ", "")
            return title

    raise RuntimeError('Missing Title')

def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def write_text_file(path, text):
    with open(path, "w", ncoding="utf-8") as f:
        f.write(text)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = read_text_file(from_path)
    template = read_text_file(template_path)
    content_node = markdown_to_html_node(markdown)
    content_html = content_node.to_html()

    title = extract_title(markdown)
    output = template.replace("{{ Title }}", title)
    output = output.replace("{{ Content }}", content_html)

    write_text_file(dest_path, output)
