from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)

def test_create_customer():
    response = client.post('/customers', json={'username': 'sweetjohn', 'address': '32, bolanle str'})
    assert response.status_code == 201
    assert response.json().get('data').get('username') == 'sweetjohn'
    assert response.json().get('data').get('address') == '32, bolanle str'

def test_get_customers():
    response = client.get('/customers')
    assert response.status_code == 200
    assert len(response.json().get('data')) == 4

def test_edit_customer():
    response = client.put('/customers/4', json={'username': 'johndanger', 'address': '40, bolanle str'})
    assert response.json().get('data').get('username') == 'johndanger'
    assert response.json().get('data').get('address') == '40, bolanle str'

