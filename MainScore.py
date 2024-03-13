"""
This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
HTML. This will be done by using python’s flask library.
"""

from flask import Flask
import jinja2
from Utils import BAD_RETURN_CODE
from Score import get_current_score

app = Flask("WorldOfGames")


@app.route('/')
def score_server():
    current_score = get_current_score()
    if current_score == BAD_RETURN_CODE:
        error_html_file = open("templates/error.html", "r")
        error_html_content = error_html_file.read()
        template = jinja2.Template(error_html_content)

        return template.render({'error': "Failed to read a score"})

    # success
    score_html_file = open("templates/score.html", "r")
    score_html_content = score_html_file.read()
    template = jinja2.Template(score_html_content)

    return template.render({'score': current_score})


app.run(host='0.0.0.0')
