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

@app.route('/api/chat/completions', methods=['POST'])
def chat_completions():
    """OpenAI-compatible chat completions endpoint"""
    
    # Get the request data
    data = request.get_json()
    
    # Basic validation for required fields
    if not data:
        return jsonify({
            "error": {
                "message": "Request body is required",
                "type": "invalid_request_error",
                "param": None,
                "code": "invalid_request"
            }
        }), 400
    
    if 'messages' not in data:
        return jsonify({
            "error": {
                "message": "Missing required field: 'messages'",
                "type": "invalid_request_error",
                "param": "messages",
                "code": "invalid_request"
            }
        }), 400
    
    if 'model' not in data:
        return jsonify({
            "error": {
                "message": "Missing required field: 'model'",
                "type": "invalid_request_error",
                "param": "model",
                "code": "invalid_request"
            }
        }), 400
    
    # Extract request parameters
    messages = data.get('messages', [])
    model = data.get('model', 'gpt-3.5-turbo')
    max_tokens = data.get('max_tokens', 100)
    temperature = data.get('temperature', 1.0)
    stream = data.get('stream', False)
    
    # Generate mock response content
    user_message = ""
    if messages and len(messages) > 0:
        last_message = messages[-1]
        if isinstance(last_message, dict) and 'content' in last_message:
            user_message = last_message['content']
    
    mock_response_content = f"This is a mocked response to: '{user_message}'. Your Flask API chat/completions endpoint was successfully called with model '{model}'. No real OpenAI integration is configured yet."
    
    # Mock response following OpenAI chat completions format
    import time
    response_data = {
        "id": f"chatcmpl-test{int(time.time())}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": model,
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": mock_response_content
            },
            "logprobs": None,
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": max(10, len(str(messages)) // 4),
            "completion_tokens": len(mock_response_content) // 4,
            "total_tokens": max(10, len(str(messages)) // 4) + len(mock_response_content) // 4
        },
        "system_fingerprint": "fp_mock_flask_api"
    }
    
    return jsonify(response_data)

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
