from logger import *
import shutil
import os

logger = Logger()


def move_all(source, inside,override=False,destination=False):
    if destination:
        for content in os.listdir(source):
            if check_exists(inside + content) and not override:
                raise Exception(f"{inside + content} already exists, -o to override")

            elif not check_exists(inside):
                raise Exception(f"{inside} not exist")
            else:
                if check_exists(inside + content):
                    os.remove(inside + content)
                shutil.move(source + content, inside)
                logger.log(f"Moved {content} -> {inside}")
    else:
        shutil.move(source,inside)

def move(source, inside,override=False):
    split_path=source.split("/")
    last=split_path.pop()
    if not check_exists(inside):
        raise Exception(f"{inside} not exist")

    if not check_exists(source):
        raise Exception(f"{source} not exist")

    if check_exists(inside + last) and not override:
        raise Exception(f"{inside+last} already exists, -o to override")

    else:
        if check_exists(inside + last):
            os.remove(inside+last)
        shutil.move(source,inside)
        logger.log(f"Has Moved {source} -> {inside}")


def rename(source, inside,override=False):
    if check_exists(inside) and not override:
        raise Exception(f"{inside} already exists, -o to override")

    elif not check_exists(source):
        raise Exception(f"{source} not exist")

    else:
        os.rename(source, inside)
        logger.log(f"Renamed {source} -> {inside}")

def check_exists(path):
    path_exist = True
    if not os.path.exists(path):
        path_exist = False
    return path_exist