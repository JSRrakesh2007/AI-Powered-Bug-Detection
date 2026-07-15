"""
AI-Powered Bug Detection

This program scans a Python file and detects
basic syntax errors automatically.
"""

import ast

INPUT_FILE = "sample_code.py"

try:
    with open(INPUT_FILE, "r") as file:
        code = file.read()

    ast.parse(code)

    result = "No syntax errors found."

except SyntaxError as e:
    result = (
        f"Bug Detected!\n\n"
        f"Line Number : {e.lineno}\n"
        f"Error Type  : Syntax Error\n"
        f"Description : {e.msg}"
    )

with open("bug_report.txt", "w") as report:
    report.write(result)

print(result)
print("\nBug report saved successfully.")