from flask import Flask

app = Flask(__name__)

# Задание 1


@app.route('/hello')
def hello():
    return 'Hello, world!'


@app.route('/info')
def info():
    return 'This is an informational page.'


# Задание 2

@app.route('/calc/<num1>', defaults={'num2': None})
@app.route('/calc/<num1>/<num2>')
def calc(num1, num2):
    if num2 is None:
        return f'Необходимо ввести два значения'
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return f'Оба значения {num1} и {num2} должны быть числами'
    return f'The sum of {num1} and {num2} is {num1 + num2}.'


# Задание 3

@app.route('/reverse/', defaults={'word': None})
@app.route('/reverse/<word>')
def reverse(word):
    if not word:
        return 'Строка должна содержать хотя бы один символ', 400
    return f'{word} -> {word[::-1]}'


# Задание 4

@app.route('/user/<name>/<age>')
def hello_user(name, age):
    try:
        age = int(age)
    except ValueError:
        return f'Возраст должен быть числом'
    if age <= 0:
        return 'Неверный возраст'
    return f'Hello, {name}. You are {age} years old.'


if __name__ == "__main__":
    app.run(debug=True)

