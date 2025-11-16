#!/usr/bin/env python3
"""Simple syntax validation of all modules"""

import sys
import os

def check_syntax():
    """Check syntax of all Python files"""
    import py_compile
    import glob
    
    files = glob.glob('/workspaces/Refactored-calculus/src/**/*.py', recursive=True)
    files += ['/workspaces/Refactored-calculus/main.py', '/workspaces/Refactored-calculus/demo.py']
    
    print("Checking Python syntax...\n")
    
    errors = []
    for f in files:
        try:
            py_compile.compile(f, doraise=True)
            print(f"✓ {f.replace('/workspaces/Refactored-calculus/', '')}")
        except py_compile.PyCompileError as e:
            print(f"✗ {f}: {e}")
            errors.append(f)
    
    if not errors:
        print("\n✅ All files have valid Python syntax!")
    else:
        print(f"\n❌ {len(errors)} file(s) with syntax errors")
    
    return len(errors) == 0

if __name__ == "__main__":
    check_syntax()
