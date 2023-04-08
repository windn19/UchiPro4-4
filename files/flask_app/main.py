from flask import Flask, render_template

app = Flask(__name__)

context1 = {'title': 'Заголовок',
            'text': 'Текст'}


@app.route('/')
def index():
    return render_template(
        'index.html'
    )


@app.route('/dict')
def dict_index():
    return render_template('index1.html', context=context1)


if __name__ == '__main__':
    app.run(debug=True)
