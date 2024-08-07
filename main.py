#Задание 1
#Создайте новое приложение Flask,
# которое будет отображать текущие дату и время на главной странице.
#Задание 2
#Создайте новое приложение Flask, создайте структуру проекта с папками static и templates,
# в папке templates должны быть 3 html файла: index, blog, contacts (главная страница, страница блога и контакты).
# Заполните их информацией и выведите силами flask сервера, используя функцию render_template()
#Обязательно на всех страницах сделайте меню, которое будет работать именно при запуске проекта через flask
from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Текущая дата и время</title>
        </head>
        <body>
            <h1>Текущая дата и время:</h1>
            <p>{{ time }}</p>
        </body>
        </html>
    ''', time=current_time)

if __name__ == '__main__':
    app.run(debug=True)