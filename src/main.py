import sys
from copy_files import copy_files, delete_files
from generate_pages import generate_page, generate_pages_recursive

def logger(text):
    print(text)

def main():

    # Set base path
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    delete_files('./public', logger, False)
    copy_files('./static', './public', logger, False)

    generate_pages_recursive(base_path, "./content", "./template.html", "./public", logger, False)

if __name__ == "__main__":
    main()