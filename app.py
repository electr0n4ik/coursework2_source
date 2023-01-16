from flask import Flask, request, render_template, jsonify, redirect
from utils import *
import logging
import json

# Импортируем блюпринты из их пакетов
from main.main_page import main_blueprint
from post_show.post_show import post_show_blueprint

app = Flask(__name__)
# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False

# Регистрируем блюпринт главной страницы GET /
app.register_blueprint(main_blueprint)
# Регистрируем блюпринт с обработкой запроса при обращении к GET /post
app.register_blueprint(post_show_blueprint)

# logging.basicConfig(filename="D:\Python\Projects\coursework2_source\logs/api.log",
#                     level=logging.INFO,
#                     format="%(asctime)s [%(levelname)s] %(message)s", encoding="utf-8")


@app.route("/search", methods=["GET", "POST"])
def search_page():
    """
    Поиск и вывод постов при обращении на GET /search/?s=...
    """
    s = request.values.get("s")  # можно делать поиск через форму "найти" и через адресную строку

    if len(list(s)) == 0 or s.isdigit():  # обработка пустого или с цифрой запроса
        return render_template("search_empty.html")

    else:
        s_list = s.split()
        for symbol in s_list:
            if symbol.isalpha():
                return render_template("search.html", s=s, posts=search_for_posts(s),
                                       amount_posts=len(search_for_posts(s)))
            else:
                return render_template("search_empty.html")


@app.route("/users/<username>")
def user_page(username):
    """
    Вывод постов конкретного пользователя GET /users/<username>
    """
    return render_template("user_feed.html", posts=get_posts_by_user(username))


@app.errorhandler(404)
def error_404(error):
    """
    Представление для ошибки "Страница не найдена"
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Представление для ошибки "Внутренняя ошибка сервера"
    """
    return render_template("500.html"), 500


@app.route("/api/posts")
def posts_in_json():
    """
    Представление для получения JSON-файла с постами
    """
    logging.info("Запрос /api/posts")
    return jsonify(get_posts_all())


@app.route("/api/posts/<post_id>")
def one_post_in_json(post_id):
    """
    Представление для получения JSON-файла с постом
    """
    logging.info(f"Запрос /api/posts/{post_id}")
    return jsonify(get_post_by_pk(post_id))


@app.route("/tag/<tagname>")
def tags_page(tagname):
    """
    Вывод постов по тегу GET /tag/<tagname>
    """
    posts = get_posts_all()
    posts_to_page = []
    for post in posts:
        if "#" + tagname in post["content"]:
            posts_to_page.append(post)
            content = get_tags(post["content"])

    return render_template("tag.html", tagname=tagname, posts=posts_to_page, content=content)

@app.route("/bookmarks/add/<postid>")
def add_page_bookmarks(postid):
    """
    Добавление в закладки по маршруту bookmarks/add/postid
    """
    posts = get_posts_all()

    for post in posts:
        if str(post["pk"]) == postid:
            with open("./data/bookmarks.json", "a", encoding="utf-8") as file:
                file.dump(list(post), file)
                break

    return redirect("/")


@app.route("/bookmarks/remove/<postid>")
def remove_page_bookmarks(postid):
    """
    Удаление из закладок по маршруту bookmarks/remove/postid
    """
    with open("./data/bookmarks.json", encoding="utf-8") as file:
        posts = file.read()
    return posts


@app.route("/bookmarks")
def get_bookmarks():
    """
    Вывод всех постов из избранного списка
    """
    with open("./data/bookmarks.json", encoding="utf-8") as file:
        posts = json.load(file)
    if len(posts) == 0:
        return render_template("bookmarks_empty.html")
    else:
        return render_template("bookmarks.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
