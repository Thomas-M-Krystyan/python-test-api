@echo off
echo Setting up Python Flask API...
echo.

echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup complete! To run the application:
echo 1. Activate the virtual environment: .venv\Scripts\activate
echo 2. Run the app: python app.py
echo.
echo Or simply run: .venv\Scripts\python.exe app.py
pause
