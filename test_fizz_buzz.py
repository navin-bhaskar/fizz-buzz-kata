from typing import List
from unittest import TestCase

from fizz_buzz import fizz_buzz


class TestFizzBuzz(TestCase):
    def test__fizz_buzz_is_called__fizz_buzz_returns_string_in_expected_format(self):
        """Reqs: Write a program that prints one line for each number from 1 to 100
                Usually just print the number itself.
                For multiples of three print Fizz instead of the number
                For the multiples of five print Buzz instead of the number
                For numbers which are multiples of both three and five print FizzBuzz instead of the number"""
        out_str: str = fizz_buzz()
        out_str_list: List[str] = out_str.split("\n")

        for idx in range(0, 100):
            cur_str = out_str_list[idx]
            cur_num = idx + 1
            if cur_num % 3 == 0:
                self.assertEqual(cur_str, "Fizz")
            elif cur_num % 5 == 0:
                self.assertEqual(cur_str, "Buzz")
            elif cur_num % 3 == 0 and cur_num % 5 == 0:
                self.assertEqual(cur_str, "FizzBuzz")
            else:
                self.assertEqual(int(cur_str), cur_num)

