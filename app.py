from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('main/index.html')

@app.route('/quiz')
def quiz():
    render_template('quiz/quiz.html')
