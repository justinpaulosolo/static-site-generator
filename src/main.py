import os
import shutil

from copystatic import copy_files_recursive
from generate import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public dir...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying files to public dir..")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(dir_path_content,template_path,dir_path_public)


main()
