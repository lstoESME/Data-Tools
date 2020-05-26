"""
Exercise 3: COUNTDOWN - Level Medium

Do you know the countdown TV show? "Des chiffres et des lettres" in french.
In this show there is a part where candidates have to find the combinations of numbers and operations in order to
approach a result.

For example Given the numbers: 11 2 101 37
We want to approach the number: 150
We can use each number only one time, and we have to use all numbers.
We can use any operation in: + - * /

The optimal result is: [(101 - 37) + 11] * 2 = 150


Your goal is to build a Countdown generator.
You will have to create the 3 following function and add their respective unit test (and docstrings).

"""


def generate_numbers_list(n):
    pass


def generate_random_operations(m):
    pass


def generate_result(numbers_list, operations_list):
    pass


def countdown_workflow(n=5):
    """
    This function is the whole workflow of our countdown algorithm, it will just call all the previous functions.

    :param n: Number of numbers to generate (default is 5)
    :return: A dict with all necessary values to do a Countdown game.
    :rtype: dict
    """
    m = n - 1
    numbers_list = generate_numbers_list(n)
    operations_list = generate_random_operations(m)
    result = generate_result(numbers_list, operations_list)

    return {'numbers': numbers_list, "result": result}
