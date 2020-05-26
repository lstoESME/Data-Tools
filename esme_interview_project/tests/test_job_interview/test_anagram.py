import unittest

from esme_lessons.job_interview.anagrams import anagram


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        # Given
        n=-'68169'
        expected_output =68169
        # When
        output=anagram(n)
        # Then
        assert expected_output == output

def test_anagram_negative() :
    # Given
    n=-1
    expected_output =None
    # When
    output=anagram(n)
    # Then
    assert expected_output == output
