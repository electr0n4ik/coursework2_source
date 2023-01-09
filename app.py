from flask import Flask, request, render_template, send_from_directory
from utils import *

# Импортируем блюпринты из их пакетов
from main.main_page import main_blueprint
from post_show.post_show import post_show_blueprint


# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
# # Чтобы заработала кириллица
# app.config['JSON_AS_ASCII'] = False

# Регистрируем первый блюпринт
app.register_blueprint(main_blueprint)
# Регистрируем второй блюпринт
app.register_blueprint(post_show_blueprint)

# @app.route('/search', methods=["POST"])
# def search_page():
#     s = request.form("s").lower()
#     return render_template("post_list.html", s=s, posts=get_posts(s))

if __name__ == "__main__":
	app.run()