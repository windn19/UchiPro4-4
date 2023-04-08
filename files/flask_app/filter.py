from flask import Flask, render_template


app = Flask(__name__)
cxt = {'text': '"""Класс для управления ресурсами и поведением игры"""',
       'tag': '<h1>Заголовок1</h1>'}


@app.get('/')
def index():
    return render_template('filter.html', **cxt)


if __name__ == '__main__':
    app.run(debug=True)