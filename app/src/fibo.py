"""
This module contains a function to generate a Fibonacci sequence of a given
length.

The main function in this module is `fibonacci(n)`, which returns a list of the
first `n` numbers in the Fibonacci sequence.

Example:
    import fibo
    sequence = fibo.fibonacci(10)
    print(sequence)  # Prints: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""


def fibonacci(n):
    """
    Generate a fibonacci sequence of length n
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence
