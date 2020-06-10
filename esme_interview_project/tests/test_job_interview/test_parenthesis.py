import unittest

from esme_lessons.job_interview.parenthesis import parenthesis, brackets


class TestParenthesis(unittest.TestCase):
    def test_parenthesis(self):
        # Given
        s = '()(()())'
        expected_result = True

        # When
        result = parenthesis(s)

        # Then
        self.assertEqual(expected_result, result) 
        #Verifier que expected_result = result


    def test_brackets(self):
        # Given
        # When
        # Then
        pass