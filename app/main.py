import os
from scripts.input_parser import parser
from scripts.tree_generator import TreeGenerator


if __name__ == '__main__':
    args = parser.parse_args()
    if not os.path.isdir(args.root_dir):
        parser.error(f"Директория не найдена: {args.root_dir}")

    tree_generator = TreeGenerator(
        root_dir=args.root_dir, 
        max_depth=args.max_depth, 
        read_gitignore=True if args.gitignore_path else False, 
        include_files=args.include_files, 
        gitignore_path=args.gitignore_path)

    output = tree_generator.generate_json() if args.output_type == 'json' else tree_generator.generate_str() 
    print(output)
