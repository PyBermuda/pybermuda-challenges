import pytest
import fibonacci as f

def test_can_calculate_fib_0():
    assert f.fibonacci(1) == 0  

def test_can_calculate_fib_1():
    assert f.fibonacci(2) == 1  

def test_can_calculate_fib_2():
    assert f.fibonacci(3) == 1  

def test_can_calculate_fib_3():
    assert f.fibonacci(4) == 2  

def test_can_calculate_fib_4():
    assert f.fibonacci(5) == 3  

def test_can_calculate_fib_5():
    assert f.fibonacci(6) == 5  

def test_can_calculate_fib_6():
    assert f.fibonacci(7) == 8  

def test_can_calculate_fib_negative_fib():
    expected_message = "This Fibonacci sequence is only defined for the natural numbers."
    with pytest.raises(Exception) as e:
        f.fibonacci(0)
    assert str(e.value) == expected_message

def test_can_calculate_fib_negative_fib():
    expected_message = "This Fibonacci sequence is only defined for the natural numbers."
    with pytest.raises(Exception) as e:
        f.fibonacci(-3)
    assert str(e.value) == expected_message

def test_can_pass_test():
    f.check_fibonacci()

def naive_implementation(n: int) -> int:
    memo = {}

    def calc(n: int) -> int:
        if n < 0:
            raise Exception("This Fibonacci sequence is only defined for the natural numbers.")
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n not in memo:
            memo[n] = calc(n - 1) + calc(n - 2)
        return memo[n]
    return calc(n)

def test_can_evaluate_fib():
    for i in range(1, 101):
        assert f.fibonacci(i) == naive_implementation(i)