#!/bin/bash
# Clean and test flooring calculator

cd /workspaces/Refactored-calculus

# Clear Python cache
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null

echo "Cache cleared. Running tests..."
echo ""

# Try running the application
python3 main.py
