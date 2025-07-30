import os
from pathlib import Path


class TreeGenerator():
    def __init__(self, 
                 ignore_list: list = [], 
                 read_gitignore: bool = True, 
                 gitignore_path: str = '.gitignore', 
                 readme_path: str = 'README.md'):
        self.ignore_list = ignore_list
        self.read_gitignore = read_gitignore
        self.readme_path = readme_path
        
        with open(gitignore_path) as file:
            if read_gitignore:
                for line in file.readlines():
                    if line[0] == '#':
                        continue
                    self.ignore_list.append(line.strip().replace('/', ''))


    def draw_tree(self, path: str):
        def ignore_condition(dir: str):
            return dir not in self.ignore_list and not dir.startswith(('.', '_')) 
        
        with open(self.readme_path, 'at', encoding="UTF-8") as file:
            file.write("# Directory tree\n\n```")
            for dirpath, dirnames, filenames in os.walk(path):
                dirnames[:] = [d for d in dirnames if ignore_condition(d)]
                filenames[:] = [f for f in filenames if not f.startswith(('_'))]
                depth = len(Path(os.path.relpath(dirpath, Path(path))).parents)
                rel_path = os.path.relpath(dirpath, path)
                has_siblings = False

                if rel_path != '.':
                    parent_path = "\\".join(dirpath.split('\\')[0:-1])
                    _, sibling_dirs, _ = next(os.walk(parent_path))
                    sibling_dirs = [d for d in os.listdir(parent_path) 
                                    if ignore_condition(d) 
                                    and os.path.isdir(os.path.join(parent_path, d))]
                    
                    sibling_dirs.remove(Path(dirpath).name)
                    has_siblings = len(sibling_dirs) > 0
                
                indent = '│   ' * (depth)
                need_indent = True
                if depth == 0:
                    dir_start_symbol = "" 
                elif not has_siblings:
                    dir_start_symbol = "└── "
                else:
                    dir_start_symbol = "├── "

                if len(dirnames) == 0 and not has_siblings:
                    need_indent = False

                file.write(f"{indent}{dir_start_symbol}{os.path.basename(dirpath)}/\n")
                for j, filename in enumerate(filenames):
                    file_start_symbol = "└── " if j == len(filenames) - 1 and len(dirnames) == 0 else "├── "
                    indent = '│   ' * (depth + 1) if need_indent else f"{'│   ' * (depth)}    "  
                    file.write(f"{indent}{file_start_symbol}{filename}\n")

                self.ignore_list.append(Path(dirpath).name)
            file.write('```')



# # curr_dir = input("Input curr directory path:")
curr_dir = r"C:\Users\matve\api_creater"
tree_generator = TreeGenerator(readme_path='README.md')
tree_generator.draw_tree(curr_dir)
