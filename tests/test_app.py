import pytest
from app import app

def test_fetch_data():
    client = app.test_client()
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.data == b'Data fetched and cached successfully!'