import argparse


parser = argparse.ArgumentParser(
    description="Generate a directory tree.", 
    epilog="Примеры:\n"
           "  python script.py --root_dir . --max_depth 2\n"
           "  python script.py --root_dir /project --read_gitignore True")

parser.add_argument(
    '--root_dir', 
    '-d',
    type=str, 
    required=True, 
    help="Absolute path to directory. Required argument")

parser.add_argument(
    '--max_depth', 
    '-m',
    type=int, 
    default=None, 
    help="Maximum scanning depth (Integer). None=No restrictions.")

parser.add_argument(
    '--no_files', 
    '-f',
    action='store_false', 
    dest='include_files', 
    help="Include files in tree (True/False)")

parser.add_argument(
    '--gitignore_path', 
    type=str, 
    default=None, 
    help="Absolute path to gitignore. Ignore files/dirs from gitignore.")

parser.add_argument(
    '--output_type', 
    '-t',
    type=str, 
    choices=['str', 'json'], 
    default='str', 
    help="Set the type of output. JSON or str")