# To create a python script to search for a file and then search for a file with specific extension.
# (Here .py our specific extension)

import os
import argparse
my_parser = argparse.ArgumentParser(description='Reading the directory path to find the file')
my_parser.add_argument("pathname", help='Please enter the directory path, where you want to search')
#my_parser.add_argument("filesearch", help='Please enter the filename to search')
args = my_parser.parse_args()

for dirname, dirpath, filename in os.walk(args.pathname):
    for file in filename:
        if file.endswith(".py"):
            print(os.path.join(dirname,file))