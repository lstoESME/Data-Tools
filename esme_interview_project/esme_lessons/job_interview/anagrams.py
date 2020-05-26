"""
Exercise 1: ANAGRAMS - Level Easy

Your goal is to write a function and it's unit test.
This function should do the following task:

Given a positive number n from 0 to an infinite value, the function should return a number
that is the highest anagram of n.

Examples:
    n = 68169
    anagram(n)
    -> 98661

    n = 1993
    anagram(n)
    -> 9931

    n = 631
    anagram(n)
    -> 631

    n = 2
    anagram(n)
    -> 2
Try to find an optimal way of doing it if possible ;)
"""


def anagram(n):
    """
    Given a positive number the function returns a number that is the highest anagram.
    :param String n: A positive number
    :return: The biggest anagram of n.

    :rtype: int
    """
    n = str(n)
    if int(n) < 0:
        return None
    else :
        n_list = [int(number) for number in n]
        output = ''
        while len(n_list) != 0:
            max_value = max(n_list)
            index_max = n_list.index(max_value)
            output += str(max_value)
            del n_list[index_max]
            return int(output)
    pass

