import pytest
import fibonacci as f

def test_can_calculate_fib_0():
    assert f.fibonacci(0) == 0  

def test_can_calculate_fib_1():
    assert f.fibonacci(1) == 1  

def test_can_calculate_fib_2():
    assert f.fibonacci(2) == 1  

def test_can_calculate_fib_3():
    assert f.fibonacci(3) == 2  

def test_can_calculate_fib_4():
    assert f.fibonacci(4) == 3  

def test_can_calculate_fib_5():
    assert f.fibonacci(5) == 5  

def test_can_calculate_fib_6():
    assert f.fibonacci(6) == 6  