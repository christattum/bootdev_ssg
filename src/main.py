from copy_files import copy_files, delete_files
from generate_pages import generate_page, generate_pages_recursive

def logger(text):
    print(text)

def main():
    delete_files('./public', logger, False)
    copy_files('./static', './public', logger, False)

    # generate_page("./content/index.md", "./template.html", "./public/index.html", logger, False)
    generate_pages_recursive("./content", "./template.html", "./public", logger, False)

if __name__ == "__main__":
    main()