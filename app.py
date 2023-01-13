from flask import Flask, request, render_template, send_from_directory
from utils import *

# Импортируем блюпринты из их пакетов
from main.main_page import main_blueprint
from post_show.post_show import post_show_blueprint


# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
# Чтобы заработала кириллица
app.config['JSON_AS_ASCII'] = False

# Регистрируем первый блюпринт
app.register_blueprint(main_blueprint)
# Регистрируем второй блюпринт
app.register_blueprint(post_show_blueprint)

@app.route("/search", methods=["GET", "POST"])
def search_page():
    """
    Поиск и вывод постов при обращении на GET /search/?s=...
    """
    s = request.values.get("s") # можно делать поиск через форму "найти" и через адресную строку

    if len(list(s)) == 0 or s.isdigit(): # обработка пустого или с цифрой запроса
        return render_template("search_empty.html")

    else:
        s_list = s.split()
        for symbol in s_list:
            if symbol.isalpha():
                # logging.info(f"Выполнен поиск по запросу {s}") # логирование при выполнении поиска
                return render_template("search.html", s=s, posts=search_for_posts(s), amount_posts=len(search_for_posts(s)))
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
    return render_template("404.html"), 404


@app.errorhandler(500)
def error_500(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
	app.run()
