#!/bin/bash
echo "Setting up Python Flask API..."
echo

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo
echo "Adding py.typed marker to aidial_sdk for type checking support..."
if [ -d ".venv/lib/python*/site-packages/aidial_sdk" ]; then
    touch .venv/lib/python*/site-packages/aidial_sdk/py.typed
    echo "Successfully added py.typed marker to aidial_sdk package."
else
    echo "Warning: aidial_sdk package not found. Skipping py.typed marker."
fi

echo
echo "Setup complete! To run the application:"
echo "1. Activate the virtual environment: source .venv/bin/activate"
echo "2. Run the app: python app.py"
echo
echo "Or simply run: .venv/bin/python app.py"
echo
echo "Note: py.typed marker added to resolve type checking warnings."
