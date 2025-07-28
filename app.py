from flask import Flask, jsonify

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Simple Hello World endpoint"""
    return jsonify({
        "message": "Hello, World!",
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

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)
