from app import app


def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert int(response.data) in range(0,101)
