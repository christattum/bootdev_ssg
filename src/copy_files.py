import os

def delete_files(target_dir: str, logger, test_mode: bool = True):

    # cwd should be the workspace root, or from where main.sh is run
    cwd = os.getcwd()
    print("Current Directory:", cwd)

    target_path = os.path.normpath(os.path.join(cwd, target_dir))
    print("Target Dir: ", target_path)

    files = os.listdir(target_path)
    for file in files:
        full_path_name = os.path.join(target_path, file)
        logger(f"Deleting {full_path_name}")


def copy_files(src_dir: str, dest_dir: str, logger, test_mode: bool = True):
    if test_mode:
        logger("Running in test mode")