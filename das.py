from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer/<title>/<surname>/<name>/<education>/<profession>/<sex>/<motivation>/<ready>')
@app.route('/auto_answer/<title>/<surname>/<name>/<education>/<profession>/<sex>/<motivation>/<ready>')
def answer(title, surname, name, education, profession, sex, motivation, ready):
    context = {
        'Фамилия': surname,
        'Имя': name,
        'Образование': education,
        'Профуссия': profession,
        'Пол': sex,
        'Мотивация': motivation,
        'Готовы остаться на Марсе?': ready,
    }
    return render_template('answer.html', title=title, contex=context)


if __name__ == '__main__':
    app.run(port=5000, host='localhost')
