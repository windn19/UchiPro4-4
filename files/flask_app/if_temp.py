from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<int:n>')
def index(n):
    return render_template(
        'Odd.html', n=n
    )


@app.route('/positiv/<n>')
def posiv_index(n):
    return render_template('positiv.html', n=int(n))


if __name__ == '__main__':
    app.run(debug=True)