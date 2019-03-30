from flask import request, jsonify

from student_performance import app
from util import database


@app.route('/info', methods=["GET"])
def index():
    user_email = request.args.get('email')
    topic = request.args.get('topic')
    subject = request.args.get('subject')

    print(f'email: {user_email}, topic: {topic}, subject: {subject}')

    student_info = database.get_student_info(user_email)
    print(f'student details: {student_info}')

    return jsonify({'status': 200})

