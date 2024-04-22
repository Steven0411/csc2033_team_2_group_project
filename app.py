from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('main/index.html')


from quiz.views import quiz_blueprint

app.register_blueprint(quiz_blueprint)
