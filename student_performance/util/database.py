import pandas as pd
import os


def get_student_info(email):
    """
    returns the student information read from the database. mock database for now.

    :param email: the email id of the student
    :return: list containing the information of the student.
    """
    data = pd.read_csv('../data/student_info/studentdb.csv')
    return data[data['email'] == email].drop('email', axis=1)
