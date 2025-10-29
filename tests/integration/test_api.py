import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from app.app import create_app

def test_api_add_success():
    app = create_app()
    client = app.test_client()

    resp = client.get('/api/add?a=4&b=5')
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.get_json()['result'] == 9

def test_api_add_invalid():
    app = create_app()
    client = app.test_client()

    resp = client.get('/api/add?a=foo&b=2')
    assert resp.status_code == 400
    assert resp.is_json
    assert 'error' in resp.get_json()
