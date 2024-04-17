from sort import sort
import random


def test_can_sort_list_in_ascending_order():
    list = [5, 3, 8, 2, 1, 4]
    assert sort(list, order='asc') == [1, 2, 3, 4, 5, 8]

def test_can_sort_list_in_descending_order():
    list = [5, 3, 8, 2, 1, 4]
    assert sort(list, order='desc') == [8, 5, 4, 3, 2, 1]

def test_sorting_alphabetical_order():
    list = ['a', 'B', 'd', 'C']
    assert sort(list, order='asc') == ['B', 'C', 'a', 'd']
    assert sort(list, order='desc') == ['d', 'a', 'C', 'B']
