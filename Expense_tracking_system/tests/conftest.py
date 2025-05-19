import sys
import os
from pathlib import Path

# Get the CORRECT project root (where your backend folder exists)
project_root = Path(__file__).parent.parent.resolve()  # Goes up to project_2
sys.path.insert(0, str(project_root))

# Verification
print("\n=== PATH DEBUGGING ===")
print(f"Project root: {project_root}")
print(f"Backend exists: {(project_root/'backend').exists()}")
print(f"db_helper exists: {(project_root/'backend'/'db_helper.py').exists()}")
print("\nUpdated Python path:")
for p in sys.path:
    print(p)