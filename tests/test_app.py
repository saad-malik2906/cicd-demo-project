import pytest
import json
from app import app, add_numbers

@pytest.fixture
def client():
    """Create a test client for our Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that homepage loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'CI/CD Pipeline Demo' in response.data

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert data['version'] == '1.1.0'

def test_api_status(client):
    """Test API status endpoint"""
    response = client.get('/api/status')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['message'] == 'API is working!'
    assert 'timestamp' in data

def test_add_numbers():
    """Test our simple function"""
    result = add_numbers(2, 3)
    assert result == 5
    
    result = add_numbers(-1, 1)
    assert result == 0

def test_add_numbers_edge_cases():
    """Test edge cases"""
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, -3) == -8
    assert add_numbers(100, 200) == 300