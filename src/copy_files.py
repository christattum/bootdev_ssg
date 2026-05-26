import os
import shutil

def delete_files(target_dir: str, logger, test_mode: bool = True):

    print()
    print(f"Deleting files from {target_dir}")
    if test_mode:
        logger("Running in test mode")

    # cwd should be the workspace root, or from where main.sh is run
    cwd = os.getcwd()
    print("Current Directory:", cwd)

    target_path = os.path.normpath(os.path.join(cwd, target_dir))
    print("Target Path: ", target_path)

    logger(f"Removing files from {target_path}")
    if not test_mode:
        shutil.rmtree(target_path)

def copy_files_r(source_path: str, target_path: str, logger, test_mode: bool = True):
    files = os.listdir(source_path)
    print(f"Files in {source_path}", files)

    # Create target directory  
    if not test_mode and not os.path.exists(target_path):
        os.mkdir(target_path)

    for file in files:
        full_source_path_name = os.path.join(source_path, file)
        full_target_path_name = os.path.join(target_path, file)
        if os.path.isdir(full_source_path_name):
            # Recurse into directory
            copy_files_r(full_source_path_name, full_target_path_name, logger, test_mode)
        elif os.path.isfile(full_source_path_name):
            # Copy file
            logger(f"Copying {full_source_path_name} to {full_target_path_name}")
            if not test_mode:
                shutil.copy(full_source_path_name, full_target_path_name)
        else:
            # May be a simlink or something else
            raise RuntimeError('Not sure what to do here!')

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

    copy_files_r(source_path, target_path, logger, test_mode)
    