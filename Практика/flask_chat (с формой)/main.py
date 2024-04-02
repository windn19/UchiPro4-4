from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

chat_messages = []


class ChatForm(FlaskForm):

    name = StringField('Имя', validators=[DataRequired(message="Поле не должно быть пустым")])
    message = TextAreaField('Сообщение', validators=[DataRequired(message="Поле не должно быть пустым")])
    submit = SubmitField('Отправить')


@app.route('/', methods=['GET', 'POST'])
def chat():
    form = ChatForm()
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data
        chat_messages.append({'name': name, 'message': message})
        return redirect(url_for('chat'))
    return render_template('index.html',
                           chat_messages=chat_messages,
                           form=form)


if __name__ == '__main__':
    app.run(debug=True)
