# Flask Test API

A simple Flask test API with welcome, chat completion, and status endpoints.

## Features

- Basic Flask API with multiple endpoints
- JSON responses
- Simple routing
- OpenAI chat completion interface mockup
- Development server configuration

## Endpoints

- `GET /` - Welcome message to Flask test API
- `POST /api/chat` - OpenAI-compatible chat completion endpoint (mocked)
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
curl -X GET http://localhost:5000/
```

### Chat Completion (OpenAI-style)
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

### Status Check
```bash
curl -X GET http://localhost:5000/api/status
```

## Browser Testing

Since the chat endpoint requires a POST request with JSON data, you cannot test it directly in a browser. However, you can:

1. **Test Welcome and Status endpoints in browser:**
   - Welcome: `http://localhost:5000/`
   - Status: `http://localhost:5000/api/status`

2. **Test Chat endpoint using browser developer tools:**
   ```javascript
   fetch('http://localhost:5000/api/chat', {
     method: 'POST',
     headers: {
       'Content-Type': 'application/json',
     },
     body: JSON.stringify({
       messages: [
         {role: 'user', content: 'Hello from browser!'}
       ]
     })
   })
   .then(response => response.json())
   .then(data => console.log(data));
   ```

3. **Use online tools like:**
   - Postman
   - Insomnia
   - HTTPie
   - Browser extensions for API testing

## Development

The application runs in debug mode by default, which means:
- Auto-reload on file changes
- Detailed error messages
- Available on all network interfaces (0.0.0.0)
