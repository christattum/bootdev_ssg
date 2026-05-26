def copy_files(src_dir: str, dest_dir: str, logger, test_mode: bool = True):
    if test_mode:
        logger("Running in test mode")