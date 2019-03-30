from flask import render_template

from student_performance import app
from core import model


@app.route('/')
def index():
    model.query()
    app.logger.warning('sample message')
    return render_template('index.html')
