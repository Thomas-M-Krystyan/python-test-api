# Python Test API (DIAL SDK)

A simple Python test API built with DIAL SDK, providing OpenAI-compatible chat completions functionality.

## Features

- DIAL SDK-based application
- OpenAI-compatible chat completions interface
- FastAPI backend with async support
- Echo functionality for testing
- Development server configuration

## Endpoints

- `GET /docs` - Interactive Swagger UI documentation for all available endpoints
- `POST /openai/deployments/python_test/chat/completions` - DIAL SDK chat completions endpoint (echo functionality)

## API Documentation

Visit `http://localhost:5002/docs` to access the interactive Swagger UI documentation. This provides a complete overview of all available endpoints with the ability to test them directly from your browser.

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

The API will be available at `http://localhost:5002`

## DIAL SDK Compatibility

The application uses the DIAL SDK framework which provides:

### Echo Application
- **Functionality**: Echoes back the last user message
- **Async processing**: Built on FastAPI with async/await support
- **OpenAI compatibility**: Full OpenAI chat completions API compatibility

### Supported Request Parameters
- **`model`**: Not required for DIAL SDK (deployment name used instead)
- **`messages`** (required): Array of message objects with `role` and `content`
- **`max_tokens`** (optional): Maximum tokens in response
- **`temperature`** (optional): Sampling temperature (0-2)
- **`stream`** (optional): Whether to stream responses

### Response Format
- Full OpenAI chat completions API compatibility
- Proper streaming support
- Contextual responses based on DIAL SDK patterns

## Usage Examples

### Chat Completions (DIAL SDK)
```bash
curl -X POST http://localhost:5002/openai/deployments/python_test/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ],
    "max_tokens": 150,
    "temperature": 0.7
  }'
```

### PowerShell Example
```powershell
$body = @{
    messages = @(
        @{
            role = "user"
            content = "Hello from PowerShell!"
        }
    )
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Uri "http://localhost:5002/openai/deployments/python_test/chat/completions" -Method POST -Body $body -ContentType "application/json"
```

## Browser Testing

### JavaScript Example (Browser Developer Console)
```javascript
fetch('http://localhost:5002/openai/deployments/python_test/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
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

### Online Tools
- Postman
- Insomnia
- HTTPie
- Browser extensions for API testing

## Development

The application uses DIAL SDK with the following features:
- **Async/await support**: Built on FastAPI for high performance
- **Auto-reload**: Development server restarts on file changes
- **Port 5002**: Runs on http://localhost:5002 by default
- **Echo functionality**: Returns the last user message content
- **Type checking support**: py.typed marker automatically added during setup

## DIAL SDK Features

- **ChatCompletion class**: Abstract base class for AI applications
- **Request/Response objects**: Structured handling of chat requests
- **Single choice responses**: Simplified response generation
- **Content streaming**: Built-in support for streaming responses
