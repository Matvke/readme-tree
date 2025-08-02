# readme-tree

A Python tool to generate directory structures with customizable filtering (`.gitignore` support) and output formats (text/JSON).

## Features
 - Recursive directory traversal with depth control
 - Flexible filtering:
    - `.gitignore` support (optional)
    - Custom ignore lists
    - File inclusion/exclusion toggle
 - Multiple output formats:
    - text
    - JSON
- CLI interface

## Usage 

**Basic command**
`python app/main.py --root_dir /path/to/directory`

### Full Options

| Argument            | Description                                  | Default      | Required |
|---------------------|----------------------------------------------|--------------|----------|
| `--root_dir`        | Root directory to scan                       | -            | Yes      |
| `--max_depth`       | Maximum recursion depth                      | None         | No       |
| `--include_files`   | Include files in output                      | True         | No       |
| `--gitignore_path`  | Custom path to `.gitignore`                  | .gitignore   | No       |
| `--output_type`     | Output format (`str` or `json`)              | str          | No       |

### Examples

1. Simple tree (text output):
   ```bash
   python tree_generator.py --root_dir ./project
   ```

2. JSON output with depth limit:
   ```bash
   python tree_generator.py --root_dir ./project --max_depth 2 --output_type json
   ```

3. With gitignore support:
   ```bash
   python tree_generator.py --root_dir ./project --gitignore_path .gitignore True
   ```

## Output Samples

**Text format:**
```
readme-tree\ 
├── app\
│   ├── scripts\
│   │   ├── input_parser.py
│   │   └── tree_generator.py
│   └── main.py
├── LICENSE
└── README.md
```

**JSON format:**
```json
{
  "readme-tree": {
    "app": {
      "scripts": {
        "input_parser.py": null,
        "tree_generator.py": null
      },
      "main.py": null
    },
    "LICENSE": null,
    "README.md": null
  }
}
```
