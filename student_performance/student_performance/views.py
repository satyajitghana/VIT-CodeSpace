from flask import render_template
from flask import request

from student_performance import app


@app.route('/')
def index():
    var = request.args.get('id')
    print(var)
    app.logger.warning('sample message')
    return render_template('index.html')
