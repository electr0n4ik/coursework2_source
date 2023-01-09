import pytest
from utils import get_post_by_pk

# 5
@pytest.mark.parametrize("post_pk_test, expected", [("", "Пост не найден!"), ("кот", "Пост не найден!"), (1, get_post_by_pk(1))])
def test_get_post_by_pk(post_pk_test, expected):
    """
    ТЕСТ: Возвращает один пост по его идентификатору.
    """
    assert get_post_by_pk(post_pk_test) == expected, f"Ошибка для ->{post_pk_test}"

