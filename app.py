from flask import Flask, jsonify, request

# Create Flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    """The initial welcome endpoint"""

    return jsonify({
        "message": "Welcome to the Flask test API!",
        "status": "success"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """OpenAI chat completion interface endpoint"""
    
    # Get the request data
    data = request.get_json()
    
    # Basic validation
    if not data or 'messages' not in data:
        return jsonify({
            "error": {
                "message": "Missing required field: messages",
                "type": "invalid_request_error"
            }
        }), 400
    
    # Mock response following OpenAI format
    return jsonify({
        "id": "chatcmpl-test123",
        "object": "chat.completion",
        "created": 1627846261,
        "model": "flask-test-model",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "This is a mocked response! Your chat endpoint was successfully called. No real OpenAI integration is configured yet."
            },
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    })

@app.route('/api/status', methods=['GET'])
def status():
    """API status endpoint"""

    return jsonify({
        "status": "running",
        "service": "Flask Hello World API",
        "version": "1.0.0"
    })

# Run the application
if __name__ == '__main__':
    # Use debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)
