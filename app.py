from flask import Flask, jsonify

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def welcome():
    """The initial welcome endpoint"""

    return jsonify({
        "message": "Welcome to the Flask test API!",
        "status": "success"
    })

@app.route('/api/hello')
def hello_api():
    """API endpoint for Hello World"""

    return jsonify({
        "message": "Hello from Flask API!",
        "endpoint": "/api/hello",
        "method": "GET"
    })

@app.route('/api/status')
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
