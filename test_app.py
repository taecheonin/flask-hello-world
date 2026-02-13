import pytest
from app import app


@pytest.fixture
def client():
    """Flask 테스트 클라이언트를 생성합니다."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    """헬로우 월드 엔드포인트를 테스트합니다."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'


def test_app_context():
    """Flask 앱이 정상적으로 생성되는지 테스트합니다."""
    assert app is not None
    assert app.config['DEBUG'] == False or app.config['DEBUG'] == True
