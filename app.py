from flask import Flask, jsonify, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

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
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
        }
        .status { 
            background: #2196F3; 
            padding: 10px; 
            border-radius: 5px; 
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 CI/CD Pipeline Demo</h1>
        <div class="status">✅ Application updated successfully!</div>
        <p><strong>Current Time:</strong> {{ current_time }}</p>
        <p><strong>Environment:</strong> {{ environment }}</p>
        <p><strong>Version:</strong> 1.1.0</p>
        <h3>Available Endpoints:</h3>
        <ul>
            <li><a href="/" style="color: #FFD700;">/</a> - Homepage</li>
            <li><a href="/health" style="color: #FFD700;">/health</a> - Health Check</li>
            <li><a href="/api/status" style="color: #FFD700;">/api/status</a> - API Status</li>
            <li><a href="/api/time" style="color: #FFD700;">/api/time</a> - Current Time</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, 
                                  current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                  environment=os.getenv('ENVIRONMENT', 'development'))

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.1.0'
    })

@app.route('/api/status')
def api_status():
    return jsonify({
        'message': 'API is working!',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/time')
def current_time():
    return jsonify({
        'current_time': datetime.now().strftime("%H:%M:%S")
    })

def add_numbers(a, b):
    return a + b

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)