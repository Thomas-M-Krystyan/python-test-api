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
echo Adding py.typed marker to aidial_sdk for type checking support...
if exist ".venv\Lib\site-packages\aidial_sdk" (
    echo. > .venv\Lib\site-packages\aidial_sdk\py.typed
    echo Successfully added py.typed marker to aidial_sdk package.
) else (
    echo Warning: aidial_sdk package not found. Skipping py.typed marker.
)

echo.
echo Setup complete! To run the application:
echo 1. Activate the virtual environment: .venv\Scripts\activate
echo 2. Run the app: python app.py
echo.
echo Or simply run: .venv/Scripts/python.exe app.py
echo.
echo Note: py.typed marker added to resolve type checking warnings.
pause
