from flask import Flask, render_template, request, redirect, flash, session
from surveys import satisfaction_survey

app = Flask(__name__)
app.secret_key = 'sdfgpsdfgpasdfg'

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/start', methods=['POST'])
def session_start():
    session["responses"] = []
    return redirect('/questions/0')

@app.route('/questions/<question_id>')
def question(question_id):
    question_id = int(question_id)
    if question_id != len(session["responses"]):
        flash("YOU TRIED TO ACCESS AN INVALID QUESTION")
        return redirect(f'/questions/{len(session["responses"])}')
    if question_id < len(satisfaction_survey.questions):
        question_text = satisfaction_survey.questions[question_id].question
        choices = satisfaction_survey.questions[question_id].choices
        return render_template('question.html', question_id=question_id, question_text=question_text, choices=choices)
    return redirect('/thank-you')

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.args.get('choice')
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses
    return redirect(f'/questions/{len(session["responses"])}')

@app.route('/thank-you')
def thanks():
    return "thanks"