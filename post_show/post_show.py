# post show
from flask import Blueprint, render_template, request, send_from_directory
from utils import *

# создаем блюпринт с настройкой папки шаблонов
post_show_blueprint = Blueprint(
	'post_show_blueprint',
	__name__,
  template_folder='templates')

@post_show_blueprint.route("/post/<post_id>")
def post_show_page(post_id):
    """
    Обработка запроса при обращении к GET /post
    """
    posts = get_posts_all()

    for post in posts:
        if int(post_id) == post["pk"]:
            get_post = post
            len_content_post = len(post["content"])
    comments = []
    amount_comments = 0
    if len(get_comments_by_post_id(post_id)) > 0:
        comments = get_comments_by_post_id(post_id)
        amount_comments = len(get_comments_by_post_id(post_id))


    return render_template("post.html", post=get_post, comments=comments, amount_comments=amount_comments, len_content_post=len_content_post)


# @loader_blueprint.route("/post", methods=["POST"]) # запрос при обращении к POST /post
# def page_add():
#     """
#     Обработка запроса при обращении к POST /post
#     """
#     import logging
#     try: # 1 обработка ошибки "Ошибка при загрузке файла"
#         photo = request.files.get("picture")
#         filename_photo = photo.filename
#         if save_photo(filename_photo): # 2 обработка ошибки "Загруженный файл - не картинка (расширение не jpeg, png, gif)"
#             text = request.form["content"]
#             photo.save(f"./uploads/{filename_photo}")
#             if save_text_in_jsonfile(filename_photo, text): # 3 обработка ошибки "Файл posts.json отсутствует или не хочет превращаться в список"
#                 return render_template("post_uploaded.html", picture=filename_photo, content=text)
#             else:
#                 return save_text_in_jsonfile(filename_photo, text)
#         else:
#             logging.info("Загруженный файл - не картинка")
#             return "Загруженный файл - не картинка (расширение не jpeg, png, gif)"
#     except:
#         logging.error("Ошибка при загрузке файла")
#         return "Ошибка при загрузке файла"
#