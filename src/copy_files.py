import os

def delete_files(target_dir: str, logger, test_mode: bool = True):

    print()
    print(f"Deleting files from {target_dir}")

    # cwd should be the workspace root, or from where main.sh is run
    cwd = os.getcwd()
    print("Current Directory:", cwd)

    target_path = os.path.normpath(os.path.join(cwd, target_dir))
    print("Target Path: ", target_path)

    files = os.listdir(target_path)
    for file in files:
        full_path_name = os.path.join(target_path, file)
        logger(f"Deleting {full_path_name}")


def copy_files(source_dir: str, target_dir: str, logger, test_mode: bool = True):

    print()
    print(f"Copying files from {source_dir} to {target_dir}")
    if test_mode:
        logger("Running in test mode")

    # cwd should be the workspace root, or from where main.sh is run
    cwd = os.getcwd()
    print("Current Directory:", cwd)

    source_path = os.path.normpath(os.path.join(cwd, source_dir))
    print("Source Path: ", source_path)

    target_path = os.path.normpath(os.path.join(cwd, target_dir))
    print("Target Path: ", target_path)

    