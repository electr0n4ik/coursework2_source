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
    post = get_post_by_pk(post_id)
    post_content = []
    len_content_post = len(post["content"])

    comments = []
    amount_comments = 0
    if len(get_comments_by_post_id(post_id)) > 0:
        comments = get_comments_by_post_id(post_id)
        amount_comments = len(get_comments_by_post_id(post_id))

    return render_template("post.html", post=post,
                           comments=comments,
                           amount_comments=amount_comments,
                           len_content_post=len_content_post)
