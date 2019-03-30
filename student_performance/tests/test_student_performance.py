import unittest

import student_performance


class Student_performanceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = student_performance.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to student_performance', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
