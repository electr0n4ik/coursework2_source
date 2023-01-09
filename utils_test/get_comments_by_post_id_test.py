import pytest
from utils import get_posts_all, get_comments_by_post_id

# 3
posts = get_posts_all()
list_id = []
list_id.append(range(1, len(posts) + 1))

@pytest.mark.parametrize("post_id", list_id)
def test_get_comments_by_post_id(post_id):
    """
    ТЕСТ: Возвращает комментарии определенного поста.
    Функция должна вызывать ошибку `ValueError` если такого поста нет
    и пустой список, если у поста нет комментов.
    """
    assert get_comments_by_post_id(post_id) == list(), f"Ошибка для ->{post_id}"

