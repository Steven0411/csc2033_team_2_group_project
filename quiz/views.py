from flask import Blueprint, render_template

quiz_blueprint = Blueprint('quiz', __name__, template_folder='templates')


@quiz_blueprint.route('/quiz')
def quiz():
    return render_template('quiz/quiz.html')

