"""
This module contains a function to check if a specific module is imported in a
Python file.

The main function in this module is `has_import(filename, module_name)`, which
returns a boolean indicating whether `module_name` is imported in the file
specified by `filename`.

Example:
    import check
    is_imported = check.has_import('test.py', 'os')
    print(is_imported)  # Prints: True if 'os' is imported in 'test.py',
    False otherwise
"""
import ast


def has_import(filename, module_name):
    """
    Check if a specific module is imported in a Python file.

    Args:
        filename (str): The name of the Python file to check.
        module_name (str): The name of the module to look for.

    Returns:
        bool: True if `module_name` is imported in `filename`, False otherwise.
    """
    with open(filename, "r", encoding="utf8") as file:
        tree = ast.parse(file.read())

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == module_name:
                    return True
        elif isinstance(node, ast.ImportFrom):
            if node.module == module_name:
                return True

    return False


# Usage
print(f"check for sys module: {has_import('app/src/fibo.py', 'sys')}")
print(f"check for pldmma module: {has_import('app/src/fibo.py', 'pldmma')}")
