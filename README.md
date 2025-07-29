# Flask Test API

A simple Flask test API with welcome and status endpoints.

## Features

- Basic Flask API with multiple endpoints
- JSON responses
- Simple routing
- Development server configuration

## Endpoints

- `GET /` - Welcome message to Flask test API
- `GET /api/hello` - API Hello World message
- `GET /api/status` - API status information

## Setup

### Option 1: Automated Setup (Recommended)

**Windows:**
```batch
setup.bat
```

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Setup

1. Create virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate virtual environment:
   ```bash
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

3. The API will be available at `http://localhost:5000`

## Usage Examples

### Welcome Message
```bash
curl http://localhost:5000/
```

### API Hello World
```bash
curl http://localhost:5000/api/hello
```

### Status Check
```bash
curl http://localhost:5000/api/status
```

## Development

The application runs in debug mode by default, which means:
- Auto-reload on file changes
- Detailed error messages
- Available on all network interfaces (0.0.0.0)
