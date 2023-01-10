import pytest
from app import *

def test_app_pain():

    response = app.test_client().get('/pain')
    assert response.status_code == 404
    assert response.data == render_template("index.html", posts=get_posts_all())


def test_get_post_by_pk():
    """
    ТЕСТ: Запрос к несуществующей странице /pain и вернуть статус-код 404
    """
    with pytest.pytest.raises():
        divide(True, None)
