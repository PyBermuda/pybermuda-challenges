from sort import manual_sort
import random


def test_can_sort_list_in_ascending_order():
    list = [5, 3, 8, 2, 1, 4]
    assert manual_sort(list, order="asc") == [1, 2, 3, 4, 5, 8]


def test_can_sort_list_in_descending_order():
    list = [5, 3, 8, 2, 1, 4]
    assert manual_sort(list, order="desc") == [8, 5, 4, 3, 2, 1]


def test_sorting_alphabetical_order():
    list = ["a", "B", "d", "C"]
    assert manual_sort(list, order="asc") == ["B", "C", "a", "d"]
    assert manual_sort(list, order="desc") == ["d", "a", "C", "B"]


def test_sort_really_long_list():
    size = 1_000_000
    list = []
    for i in range(size):
        list.append(random.randint(0, 1_000_000_000))

    sorted = manual_sort(list, order="asc")
    for i in range(1, size):
        assert sorted[i - 1] <= sorted[i]


def test_sort_really_long_list_including_negative_desc():
    size = 1_000_000
    list = []
    for i in range(size):
        list.append(random.randint(-1_000_000_000, 1_000_000_000))

    sorted = manual_sort(list, order="desc")
    for i in range(1, size):
        assert sorted[i - 1] >= sorted[i]


def test_sort_does_not_use_sort_or_sorted():
    with open("003/sort.py") as file:
        content = file.read()
        assert (
            "sorted(" not in content
        ), "You are not allowed to use the sorted function. Write your own sorting algorithm."
        assert (
            ".sort(" not in content
        ), "You are not allowed to use the .sort method. Write your own sorting algorithm."
