import unittest

from esme_lessons.job_interview.countdown import generate_numbers_list, generate_random_operations, generate_result, \
    countdown_workflow


"""
For this unit test we want to test each function.
But for the workflow function, we want to mock each sub-function call, checking that each function is called once,
with the output of the previous one.
We can also mock the random parts of any function if we want so.
(for example if we image tha calling one function takes 1 hour, we don't want to wait 1 hour for a unit test)
"""
from unittest.mock import patch

class TestCountdown(unittest.TestCase):
    def test_generate_numbers_list(self):
        # Given
        n = 4
        # When
        numbers_list = generate_numbers_list(n)
        # Then
        self.assertEquals(n, len(numbers_list))
        for number in numbers_list:
            self.assertIsInstance(number, int)
            self.assertLessEqual(number, 200)

    @patch("esme_lessons.job_interview.countdown.random.choices")
    def test_generate_random_operations(self, mock_random):
        # Given
        m = 3
        mock_random.return_value = ["+","-","*","/"]
        # When
        result = generate_random_operations(m)
        # Then
        mock_random.assert_call_once_with("+-*/", m)
        self.assertEqual(len(result),m)
            #vérifie que l'opérateur appartient à la liste '+-*/'

    def test_generate_result(self):
        # Given
        numbers_list = [3, 9, 20, 2]
        operations_list = ["+", "-", "+"]
        expected_result =-6
        # When
        result = generate_result(numbers_list, operations_list)
        # Then
        self.assertEqual(expected_result, result)

    @patch("esme_lessons.job_interview.countdown.generate_result")
    @patch("esme_lessons.job_interview.countdown.generate_random_operations")
    @patch("esme_lessons.job_interview.countdown.generate_numbers_list")

    def test_countdown_workflow(self, 
                                mock_generate_numbers_list, 
                                mock_generate_random_operations, 
                                mock_generate_result):
        # Given
        n=5
        mock_generate_numbers_list.return_value = [1,2,3,4,5]
        mock_generate_random_operations.return_value = ["+", "+", "+", "-"]
        mock_generate_result.return_value = 5

        result = {"numbers":  mock_generate_numbers_list.return_value,
                "result": mock_generate_result.return_value}
        # When
        expected_result = countdown_workflow
        # Then
        self.assertEqual(expected_result, result)

        mock_generate_numbers_list.assert_call_once_with(n)
        mock_generate_random_operations.assert_call_once_with(n-1)
        mock_generate_result.assert_call_once_with(
            mock_generate_numbers_list.return_value,
            mock_generate_random_operations.return_value
        )
        #Vérifier que les fonctions ont bien été appelé une et unique fois.

