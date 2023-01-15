# import pytest
# from utils import get_posts_all, get_posts_by_user
#
# # 2
# posts = get_posts_all()
# list_names = []
# for post in posts:
#     list_names.append(tuple(post["poster_name"]))
#
# @pytest.mark.parametrize("poster_name", list_names)
# def test_get_posts_by_user(poster_name):
#     """
#     ТЕСТ: Возвращает список постов по определенному пользователю.
#     Функция вызывает ошибку `ValueError`, если пользователя нет
#     и пустой список, если у пользователя нет постов.
#     """
#
#     assert get_posts_by_user(poster_name) == list(), f"Ошибка для ->{poster_name}"
#
