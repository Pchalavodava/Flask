import random

from app import app
from flask import render_template, request, redirect, url_for


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        color = get_form_value("favorite-color")
        profession = request.form.get("profession")
        hobbies = get_form_value('hobbies')
        level = request.form.get("level")
        joke = get_random_joke(jokeList)
        return render_template("result.html", name=name, email=email, color=color,
                               profession=profession, hobbies=hobbies, level=level, joke=joke)
    else:
        return redirect(url_for("form"))


def get_form_value(name):
    if name == 'hobbies':
        result = request.form.getlist(name)
    else:
        result = request.form.get(name)
    if not result:
        match name:
            case ('hobbies'):
                return "You don't have any hobbies"
            case ('favorite-color'):
                return "You don't have a favorite color"
    return result


jokeList = ['Как заставить змею плакать? — Отобрать у нее погремушку.',
            'Зачем птицы летают в теплые края? — Потому что идти пешком долго.',
            'Британские ученые выяснили: если долго смотреть на кота, он начнет смотреть в ответ… с осуждением.',
            'Почему крокодил не пишет стихи? — Слез хватает, а рифм нет.',
            'Почему рыбы живут в соленой воде? — Потому что перченая вода заставляет их чихать.',
            'Что дают балованные коровы? — Испорченное молоко.',
            'Как называют медведя без зубов? — Мармеладный мишка.',
            'Что делает улитка, когда устает? — Берет дом и уезжает.',
            'Какая любимая фраза у акулы? — Человек за бортом!',
            'Почему попугай ушел от хозяйки? — Она его перебивала.',
            'Что сказал петух, увидев будильник? — Ты что, тоже тут работаешь?',
            'Собака любит тебя просто так. Особенно, если ты с сосиской.',
            'Что делает медведь, если услышал, что скоро весна? — Переворачивается на другой бок и говорит: '
            '«Еще пять минуточек».']


def get_random_joke(jokes):
    return random.choice(jokes)
