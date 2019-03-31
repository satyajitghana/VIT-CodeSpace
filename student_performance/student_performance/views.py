from flask import request, jsonify

from student_performance import app
from src.model import model
from util import database


@app.route('/info', methods=["GET"])
def info():
    """
    returns the text required from the subject and topic given.

    :return: the information required.
    """
    # extracting information on the query
    user_email = request.args.get('email')
    topic = request.args.get('topic')
    subject = request.args.get('subject')

    print(f'email: {user_email}, topic: {topic}, subject: {subject}')

    # gathering information of the student from the database
    student_info = database.get_student_info(user_email)
    # print(f'student details: {student_info}')

    # predicting the marks of the student.
    marks = model.predict(student_info, subject)
    print(f'the marks of the student is: {marks}')

    # getting the information.
    info = database.get_info_file(subject, topic)

    # getting the text depending on the student marks.
    if marks < 20:
        info = info["Weak"]
    elif 20 <= marks <= 70:
        info = info["Average"]
    else:
        info = info["Intelligent"]

    return jsonify({'status': 200, 'info': info})

