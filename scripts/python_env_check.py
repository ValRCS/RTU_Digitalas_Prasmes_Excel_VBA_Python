"""
Python environment checker for Excel + Jupyter lesson
Checks required libraries and prints installation instructions.
"""

import importlib

required_packages = {
    "pandas": "pandas",
    "openpyxl": "openpyxl",
    "matplotlib": "matplotlib",
    "jupyter": "notebook"  # import name differs
}

missing = []

print("=== Python Environment Check ===\n")

for pkg, import_name in required_packages.items():
    try:
        importlib.import_module(import_name)
        print(f"[OK] {pkg} is installed")
    except ImportError:
        print(f"[MISSING] {pkg} is NOT installed")
        missing.append(pkg)

print("\n=== Summary ===")

if not missing:
    print("All required libraries are installed. You are ready for the lesson.")
else:
    print("Missing libraries:")
    for m in missing:
        print(f" - {m}")

    print("\nInstall them with:\n")
    print("pip install " + " ".join(missing))
    print("\nIf you are using VS Code with virtual environment:\n")
    print("1. Activate your environment")
    print("2. Run the command above in terminal")

print("\n=== Python Version ===")
import sys
print(sys.version)
