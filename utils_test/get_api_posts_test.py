import app
from app import *
import pytest

# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False

def test_app():
    response = app.test_client().get('/api/posts')

    assert type(response.json) == list

    keys_posts = response.json
    for post in keys_posts:
        # по-моему глупое выражение для теста, но мне интересно, как обойти ошибку которая будет без str типа
        # post.keys() == dict_keys(['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'])
        # так появляется ошибка NameError: name 'dict_keys' is not defined
        assert str(post.keys()) == "dict_keys(['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'])"


def test_app2():
    for post_id in range(len(get_posts_all())):
        response = app.test_client().get(f"/api/posts/{post_id}")
        keys_post = response.json

        assert type(response.json) == dict
        assert str(keys_post) == "dict_keys(['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count'])"

