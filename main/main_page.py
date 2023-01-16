# main page show
from utils import get_posts_all
from flask import Blueprint, render_template, jsonify
import json

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
    with open("./data/bookmarks.json", encoding="utf-8") as file:
        bookmarks = json.load(file)

    return render_template("index.html", posts=get_posts_all(), amount_bookmarks=len(bookmarks))