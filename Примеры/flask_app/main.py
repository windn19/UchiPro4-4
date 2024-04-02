from flask import Flask

app = Flask(__name__)

counter = 0


@app.route('/')
def index():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(debug=True)
