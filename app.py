from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/madlib_form')
def madlib():
    return render_template("madlib_form.html", prompts=story.prompts)

@app.route('/madlib')
def make_madlib():
    madlib_text = story.generate(request.args)
    return render_template("madlib.html", text=madlib_text)

    