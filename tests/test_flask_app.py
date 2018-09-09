#-*- using:utf-8 -*-
import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app

@pytest.fixture
def client(app):
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()

def test_app_config(app):
    assert ('ENV' in app.config) == True
    assert ('production' in app.config['ENV']) == True


def test_index_page(client):
    print("{}".format(client))
    res = client.get('/')
    print(''.format(res.data))
    assert res.status_code == 200
