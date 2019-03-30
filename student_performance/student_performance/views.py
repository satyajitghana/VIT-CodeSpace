from flask import render_template
from flask import request

from student_performance import app
from src.data import process_data


@app.route('/')
def index():
    var = request.args.get('id')
    print(var)
    process_data.process("data/raw", "data/processed")
    app.logger.warning('sample message')
    return render_template('index.html')
