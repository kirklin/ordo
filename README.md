# Ordo

A cross-platform tool to create a structured file organization system with a standardized classification method to solve the problem of file chaos.

*[中文文档](README.zh-CN.md)*

## Features

- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux
- **Unified Classification System**: Uses numerical coding and bilingual naming conventions
- **Hierarchical Structure**: Provides multi-level structured folder organization
- **AI-Ready**: Interface reserved for future AI integration

## Classification Method

The file management system uses a numerical classification method with 10 main categories:

- **00000000 - Inbox**: Temporary storage for files to be processed
- **10000000 - Work**: Work-related files
- **20000000 - Learning**: Educational materials
- **30000000 - Interest**: Hobbies and personal interests
- **40000000 - Memories**: Photos and memories
- **50000000 - Resource**: Resource files
- **60000000 - ArtWork**: Artistic creations
- **70000000 - MediaLibrary**: Media collection
- **80000000 - Archive**: Archived files
- **90000000 - Miscellaneous**: Files that don't fit elsewhere

Each main category contains multiple subcategories with their own numerical codes, forming a complete hierarchical structure.

## Installation

### Direct Usage
No installation required. Simply ensure your system has Python 3.6 or later installed.

### Using as a Package with UV
For a more integrated experience, you can install the package using the [uv](https://github.com/astral-sh/uv) package manager:

```bash
# Install uv if you don't have it
curl -sSf https://astral.sh/uv/install.sh | sh

# Install ordo package
uv pip install file-ordo
```

## Usage

### Using Scripts Directly
1. Download the appropriate script for your system:
   - `create_folders.py` (Python - all platforms)
   - `create_folders.sh` (Bash - macOS/Linux)
   - `create_folders.bat` (Batch - Windows)

2. Run the script:
   ```bash
   # Python (all platforms)
   python create_folders.py
   
   # Bash (macOS/Linux)
   ./create_folders.sh
   
   # Batch (Windows)
   create_folders.bat
   ```

### Using as an Installed Package
If you've installed ordo using uv:

```bash
# Simply run
ordo
```

3. Follow the prompts to choose where to create the folder structure
4. The program will automatically create the complete folder structure

## Upcoming Features

- **AI Integration**: Planned AI assistant to help automatically organize files into appropriate locations
- **GUI Interface**: Add a graphical user interface for more user-friendly operation
- **Custom Templates**: Allow users to create and save custom folder structure templates
- **File Synchronization**: Support for synchronizing folder structures across multiple devices

## License

GNU General Public License v3.0

## Author

[Kirk Lin](https://github.com/kirklin) 
