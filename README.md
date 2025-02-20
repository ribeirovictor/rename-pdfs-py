I'll create a README.md file that explains how to use these three Python files. I notice that `create_json.py` and `json_generate.py` appear to be identical files, so I'll document them as alternatives.

````markdown:/Users/ribeirovictor/Documents/work/2em1/landings/certificados/README.md
# Certificate Files Management

This repository contains Python scripts to manage and organize PDF certificate files.

## Requirements

Before using these scripts, make sure you have the following dependencies installed:

```bash
pip install PyMuPDF unidecode
````

## Scripts Description

### 1. PDF File Renaming (`rename_pdf.py`)

This script automatically renames PDF files based on their content. It:

- Reads PDF files from the `arquivos` directory
- Extracts text from the first page
- Creates a clean, formatted filename from the content
- Removes accents and special characters
- Renames the file with the new name

Usage:

```bash
python rename_pdf.py
```

### 2. File List Generation (`create_json.py` or `json_generate.py`)

These scripts (both do the same thing) create a JSON file containing a list of all files in a specified directory.

Usage:

```bash
python create_json.py
```

or

```bash
python json_generate.py
```

When prompted, enter the directory path you want to scan.

## Directory Structure

```
.
├── arquivos/         # Directory containing PDF files
├── create_json.py    # Script to generate JSON file list
├── json_generate.py  # Alternative script to generate JSON file list
├── rename_pdf.py     # Script to rename PDF files
└── files.json       # Generated JSON file containing the file list
```

## Workflow

1. Place your PDF certificates in the `arquivos` directory
2. Run `rename_pdf.py` to automatically rename the files based on their content
3. Run either `create_json.py` or `json_generate.py` to generate a JSON list of the files

## Notes

- The PDF renaming script expects files to be in the `arquivos` directory
- The JSON generation scripts will create a `files.json` file in the current directory
- Make sure you have write permissions in the directories you're working with

```

```
