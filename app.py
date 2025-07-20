from flask import Flask, jsonify, render_template_string
import os
from datetime import datetime

# Create Flask application instance
app = Flask(__name__) 

# HTML template for our homepage
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CI/CD Demo App</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
        }
        .status { 
            background: #4CAF50; 
            padding: 10px; 
            border-radius: 5px; 
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 CI/CD Pipeline Demo</h1>
        <div class="status">✅ Application is running successfully!</div>
        <p><strong>Current Time:</strong> {{ current_time }}</p>
        <p><strong>Environment:</strong> {{ environment }}</p>
        <p><strong>Version:</strong> 1.0.0</p>
        <h3>Available Endpoints:</h3>
        <ul>
            <li><a href="/" style="color: #FFD700;">/</a> - Homepage</li>
            <li><a href="/health" style="color: #FFD700;">/health</a> - Health Check</li>
            <li><a href="/api/status" style="color: #FFD700;">/api/status</a> - API Status</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Homepage route"""
    return render_template_string(HTML_TEMPLATE, 
                                current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                environment=os.getenv('ENVIRONMENT', 'development'))

@app.route('/health')
def health_check():
    """Health check endpoint - used by Docker and deployment platforms"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        'message': 'API is working!',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'timestamp': datetime.now().isoformat()
    })

def add_numbers(a, b):
    """Simple function for testing purposes"""
    return a + b

if __name__ == '__main__':
    # Get port from environment variable (used by deployment platforms)
    port = int(os.getenv('PORT', 5000))
    
    # Run the application
    app.run(host='0.0.0.0', port=port, debug=True)