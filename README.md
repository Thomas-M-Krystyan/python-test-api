# Flask Test API

A simple Flask test API with welcome, OpenAI-compatible chat completions, and status endpoints.

## Features

- Basic Flask API with multiple endpoints
- JSON responses
- Simple routing
- OpenAI chat completions interface mockup (fully compatible)
- Development server configuration

## Endpoints

- `GET /` - Welcome message to Flask test API
- `POST /api/chat/completions` - OpenAI-compatible chat completions endpoint (mocked)
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

## OpenAI Compatibility

The `/api/chat/completions` endpoint is fully compatible with OpenAI's Chat Completions API format:

### Supported Request Parameters
- **`model`** (required): Model identifier (e.g., "gpt-3.5-turbo", "gpt-4")
- **`messages`** (required): Array of message objects with `role` and `content`
- **`max_tokens`** (optional): Maximum tokens in response
- **`temperature`** (optional): Sampling temperature (0-2)
- **`stream`** (optional): Whether to stream responses

### Response Format
- Matches OpenAI's response structure
- Includes token usage statistics
- Dynamic response IDs and timestamps
- Contextual mock responses that reference user input

### Error Handling
- OpenAI-compatible error responses
- Proper HTTP status codes
- Detailed error messages with parameter information

## Usage Examples

### Welcome Message
```bash
curl -X GET http://localhost:5000/
```

### Chat Completions (OpenAI-style)
```bash
curl -X POST http://localhost:5000/api/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ],
    "max_tokens": 150,
    "temperature": 0.7
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

2. **Test Chat completions endpoint using browser developer tools:**
   ```javascript
   fetch('http://localhost:5000/api/chat/completions', {
     method: 'POST',
     headers: {
       'Content-Type': 'application/json',
     },
     body: JSON.stringify({
       model: 'gpt-3.5-turbo',
       messages: [
         {role: 'user', content: 'Hello from browser!'}
       ],
       max_tokens: 100,
       temperature: 0.7
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
