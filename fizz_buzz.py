
from typing import List


def fizz_buzz() -> str:
    result_list: List[str] = []

    for i in range(1, 101):
        if i % 3 == 0:
            result_list.append("Fizz")
        elif i % 5 == 0:
            result_list.append("Buzz")
        elif i%3 == 0 and i % 5 == 0:
            result_list.append("FizzBuzz")
        else:
            result_list.append(str(i))

    return "\n".join(result_list)
