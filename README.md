# Log Text Filter Utility

A lightweight command-line tool written in Python designed to search for specific text strings within files of a given extension. It is ideal for technical support tasks, automation, and parsing log files, allowing you to quickly extract lines containing errors, warnings, or specific keywords.

## Features
* **Directory and Extension Filtering:** Processes only the relevant files within the specified directory path.
* **Keyword Extraction:** Scans file contents and isolates lines containing the exact search string.
* **Result Consolidation:** Generates a single output file (`result_text.txt`) with all the matching lines found across the processed files.

## Requirements
* Python 3.x
* No external dependencies required (uses standard Python libraries: `sys`, `os`, `pathlib`).

## Usage

The script runs from the terminal and requires exactly 3 positional parameters:

1. `Directory`: The path to the folder where the files are located.
2. `Extension`: The file extension to parse (e.g., `.log`, `.txt`).
3. `Keyword`: The exact text string to search for within the files.

### Syntax
```bash
python script.py <directory_path> <extension> <keyword>
