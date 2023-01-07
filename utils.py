# 1
def get_posts_all():
    """
    Возвращает все посты из файла posts.json

    У каждого поста указаны:
    `poster_name` — имя/юзернейм автора поста,
    `poster_avatar` — аватарка автора поста,
    `pic` — картинка поста,
    `content` — текст поста,
    `views_count` — количество просмотров,
    `likes_count` — количество лайков,
    `pk` — id или номер поста.
    """
    import json

    with open("data/posts.json", encoding="utf-8") as file:
        posts = json.load(file)
    return posts


# 2
def get_posts_by_user(poster_name):
    """
    Возвращает список постов по определенному пользователю.
    Функция вызывает ошибку `ValueError`, если пользователя нет
    и пустой список, если у пользователя нет постов.
    """
    list_posts = []
    flag = 1
    try:
        for user in get_posts_all():
            if poster_name.lower() == user["poster_name"].lower():
                list_posts.append(user)
                if user["content"]: # если посты есть у пользователя, то
                    flag = 0
        if len(list_posts) > 0:
            return list_posts # 1
        elif flag:
            return ValueError("Пользователя не существует") # 2
    except:
        return list_posts # 3


# 3
def get_comments_by_post_id(post_id):
    """
    Возвращает комментарии определенного поста.
    Функция должна вызывать ошибку `ValueError` если такого поста нет
    и пустой список, если у поста нет комментов.
    """
    import json

    with open("data/comments.json", encoding="utf-8") as file:
        comments = json.load(file)

    list_comments = []
    flag = 1
    try:
        for comment in comments:
            if int(post_id) == comment["post_id"]:
                list_comments.append(comment)
                if comment["comment"]:  # если комментарий есть у поста, то
                    flag = 0
        if len(list_comments) > 0:
            return list_comments  # 1
        elif flag:
            return ValueError("Поста не существует")  # 2
    except:
        return list_comments  # 3


# 4
def search_for_posts(query):
    """
    Возвращает список постов по ключевому слову
    """
    list_posts = []
    for post in get_posts_all():
        if query.lower() in post["content"].lower():
            list_posts.append(post)

    if len(query) == 0 or len(list_posts) == 0:
        return "Пост не найден!"
    else:
        return list_posts


# 5
def get_post_by_pk(pk):
    """
    Возвращает один пост по его идентификатору.
    """
    post = []
    flag = 0
    for post in get_posts_all():
        if int(pk) == post["pk"]:
            return post
        else:
            flag = 1

    if flag:
        return "Пост не найден!"


# posts = get_post_by_pk(1)
# try:
#     for post in posts:
#         print(post["content"])#, end="")
#         print()
# except:
#     print(posts["content"])

