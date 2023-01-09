# main page show
from utils import *
from flask import Blueprint, render_template

# Создаем блюпринт главной страницы
# Должно показываться столько постов, сколько есть
main_blueprint = Blueprint(
	'main_blueprint',
	__name__,
  template_folder='templates')

@main_blueprint.route('/')
def main_page():
    """
    Обработка запроса при обращении к /
    """

    return render_template("index.html", posts=get_posts_all())