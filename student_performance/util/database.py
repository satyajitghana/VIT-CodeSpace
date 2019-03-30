import pandas as pd
import json


def get_student_info(email):
    """
    returns the student information read from the database. mock database for now.

    :param email: the email id of the student
    :return: list containing the information of the student.
    """

    data = pd.read_csv('data/student_info/studentdb.csv')
    return data[data['email'] == email].drop('email', axis=1)


def get_info_file(subject, topic):
    """
    returns the json data of the subject and topic given.

    :param subject: the subject whose information is required
    :param topic: the topic whose information is required.
    :return: the information
    """

    data = json.load(open(f'data/info/{subject}.json', 'rb'))
    return data[topic.lower()]

