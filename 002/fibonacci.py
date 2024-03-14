"""
NOT TERRIBLE FIBONACCI

I am sure I don't need to tell you that the Fibonacci sequence is a series of
numbers in which each numbers, starting with 0 and 1, where each value is the
sum of the two preceding ones.

The first 10 values are as follows.

Example Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Your task is to complete the `fibonacci` function below so that it will return
the 40th number in the sequence *in less than 0.5s*. 

NO YOU CANNOT JUST RETURN THE NUMBER 63,245,986 - the function must accept a
single argument `n`, and return the nth number in the sequence.

To get you started, it *might* be a good idea to make `fibonacci` a recursive
function: but note that this alone probably won't be able to perform the
calculation in less than 0.5s (unless you have a very powerful machine).
A clue to making it faster would be: each call to the (recursive) `fibonacci`
function will likely result in 2 further calls to the function (to get the
previous two numbers). This will result in a large number of calls to
retrieve the same number in the sequence. What if the function could remember
previous calculations it had performed?
"""

from time import perf_counter


def fibonacci(n) -> int:
    # write your code here 👇👇
    pass
    # write your code here 👆👆


def check_fibonacci() -> None:
    n = 40
    max_time = 1

    start = perf_counter()
    answer = fibonacci(n)

    assert (
        answer is not None
    ), "Yeah you're going to actually have to write something in the fibonacci function"

    assert (
        answer == 63245986
    ), f"Unfortunately {answer} is not the {n}th fibonacci number"

    print(f"The {n}th fibonacci number is {answer}")
    stop = perf_counter()

    elapsed = stop - start

    assert (
        elapsed < max_time
    ), f"The {n}th fibonacci number took more than {max_time}s: it took {elapsed:.2f}s"

    print(f"Done in {elapsed:.6f}s")


if __name__ == "__main__":
    check_fibonacci()
