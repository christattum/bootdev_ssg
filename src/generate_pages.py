import os
from markdown_parser import markdown_to_blocks
from markdown_to_html import markdown_to_html_node

def extract_title(markdown: str):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            title = block.replace("# ", "")
            return title

    raise RuntimeError('Missing Title')

def read_text_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def write_text_file(path: str, text: str):
    # Ensure directories exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def generate_page_paths(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = read_text_file(from_path)
    template = read_text_file(template_path)
    content_node = markdown_to_html_node(markdown)
    content_html = content_node.to_html()

    title = extract_title(markdown)
    output = template.replace("{{ Title }}", title)
    output = output.replace("{{ Content }}", content_html)

    write_text_file(dest_path, output)

def generate_page(from_dir: str, template_file: str, dest_dir: str):
    cwd = os.getcwd()
    print("Current Directory:", cwd)

    from_path = os.path.normpath(os.path.join(cwd, from_dir))
    print("From Path: ", from_path)

    template_path = os.path.normpath(os.path.join(cwd, template_file))
    print("Template Path: ", template_path)

    dest_path = os.path.normpath(os.path.join(cwd, dest_dir))
    print("Dest Path: ", dest_path)

    generate_page_paths(from_path, template_path, dest_path)

def generate_pages_recursive(from_dir: str, template_file: str, dest_dir: str):
    cwd = os.getcwd()
    from_path = os.path.normpath(os.path.join(cwd, from_dir))
    dest_path = os.path.normpath(os.path.join(cwd, dest_dir))
    template_path = os.path.normpath(os.path.join(cwd, template_file))
    files = os.listdir(from_dir)

    for file in files:
        full_from_path_name = os.path.join(from_path, file)
        full_dest_path_name = os.path.join(dest_path, file)

        if os.path.isdir(full_from_path_name):
            # Recurse into directory
            generate_pages_recursive(full_from_path_name, full_dest_path_name)
        elif os.path.isfile(full_from_path_name):
            # Generate page
            generate_page_paths(full_from_path_name, template_path, full_dest_path_name)
        else:
            # May be a simlink or something else
            raise RuntimeError('Not sure what to do here!')
