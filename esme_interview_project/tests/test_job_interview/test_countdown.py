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


class TestCountdown(unittest.TestCase):
    def test_generate_numbers_list(self):
        # Given
        n = 5
        # When
        numbers_list = generate_numbers_list(n)
        # Then
        self.assertEquals(n, len(numbers_list))
        for number in numbers_list:
            self.assertIsInstance(number, int)
            self.assertLessEqual(number, 200)

    def test_generate_random_operations(self):
        # Given
        # When
        # Then
        pass

    def test_generate_result(self):
        # Given
        # When
        # Then
        pass

    def test_countdown_workflow(self):
        # Given
        # When
        # Then
        pass

