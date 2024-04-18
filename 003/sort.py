"""
SORTING

There are many different ways to sort a list. 

This excercise will introduce the concept of unit tests.

The unit tests can be found in the file 003/test_sort.py

To run the tests simply run `pytest` in the terminal (after having done `pip install -r requirements.txt`)
"""

from time import perf_counter


def manual_sort(list: list, *, order: str) -> int:
    """
    Sorts a list in ascending or descending order based on the given order parameter.

    Args:
        list: The list to be sorted.
        order: The order in which to sort the list. Can be either "asc" for ascending order or "desc" for descending order.

    Returns:
        The sorted list.

    """
    # WRITE YOUR CODE HERE 👇👇
    list.sort(reverse=order == "desc")
    return list
    # WRITE YOUR CODE HERE 👆👆
