from flask import render_template
from flask import request

from student_performance import app
from core import model


@app.route('/')
def index():
    var = request.args.get('id')
    print(var)
    model.query()
    app.logger.warning('sample message')
    return render_template('index.html')
