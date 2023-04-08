from flask import Flask, render_template


app = Flask(__name__)
lst = ['кошка', "мышка", "собака"]
context = {'Заголовок 1': 'Текст 1',
           'Заголовок 2': 'Текст 2',
           'Заголовок 3': 'Текст 3'}


@app.get('/')
def index():
    return render_template('loop.html', lst=lst)


@app.get('/dict')
def dict_index():
    return render_template('dict_loop.html', context=context)


@app.get('/dict_loop')
def loop_index():
    return render_template('dict_loop1.html', context=context)


@app.get('/dict_else/<int:n>')
def else_index(n):
    return render_template('dict_else.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)