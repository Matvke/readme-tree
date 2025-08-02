import json
import os
from pathlib import Path


CONNECTOR_BRANCH = "├── "
CONNECTOR_LAST_BRANCH = "└── "
PREFIX_PIPE = "│   "
PREFIX_EMPTY = "    "

class TreeGenerator():
    def __init__(self, 
                 root_dir: str, 
                 max_depth: int|None = None,
                 read_gitignore: bool = True, 
                 include_files: bool = True,
                 ignore_list: list = [], 
                 gitignore_path: str = '.gitignore'):
        self.max_depth = max_depth
        self.ignore_list = ignore_list
        self.root_dir = Path(root_dir).resolve()
        self.include_files = include_files

        if read_gitignore:
            try:
                self.ignore_list.extend(self._read_gitignore(gitignore_path))
            except FileNotFoundError as e:
                print(f'File not found at "{gitignore_path}". \n {e}')

    def _read_gitignore(self, gitignore_path) -> list:
        gitignore_list = []
        with open(gitignore_path) as file:
            for line in file.readlines():
                if line[0] == '#':
                    continue
                gitignore_list.append(line.strip().replace('/', ''))
        return gitignore_list

    def _build_tree(self, curr_path, curr_depth: int = 0):
        if self.max_depth and curr_depth >= self.max_depth:
            return None
        tree = {}

        for entity in sorted(os.scandir(curr_path), key=lambda e: e.is_file()):
            path_entity = Path(entity)
            if self._is_ignored(path_entity):
                continue

            if entity.is_dir():
                tree[entity.name] = self._build_tree(path_entity, (curr_depth + 1))
            elif entity.is_file() and self.include_files:
                tree[entity.name] = None
        return tree
    
    def _format_tree(self, tree_dict: dict, prefix: str = '') -> list[str]:
        lines = []
        entities = list(tree_dict.keys())

        for i, name in enumerate(entities):
            is_last = (i == len(entities) - 1)
            connector = CONNECTOR_LAST_BRANCH if is_last else CONNECTOR_BRANCH

            if isinstance(tree_dict[name], dict):
                lines.append(f"{prefix}{connector}{name}\\")
                parent_prefix = PREFIX_EMPTY if is_last else PREFIX_PIPE
                lines.extend(self._format_tree(tree_dict[name], prefix=prefix + parent_prefix))

            else:
                lines.append(f"{prefix}{connector}{name}")

        return lines

    def _is_ignored(self, path: Path):
        return path.name in self.ignore_list or path.name.startswith(('.', '_')) 

    def generate_str(self) -> str:
        tree_structure = self._build_tree(self.root_dir)
        tree_lines = self._format_tree(tree_structure)
        return f"{self.root_dir.name}\\ \n" + "\n".join(tree_lines)

    def generate_json(self) -> str:
        tree_structure = {} 
        tree_structure[self.root_dir.name]= self._build_tree(self.root_dir)
        return json.dumps(tree_structure)