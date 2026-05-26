from copy_files import copy_files, delete_files

def logger(text):
    print(text)

def main():
    delete_files('./public', logger, False)
    copy_files('./static', './public', logger, False)

if __name__ == "__main__":
    main()