import time
import matplotlib.pyplot as plt
from math import *
from decimal import Decimal, Context


def fibonacci_1(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


def fibonacci_2(n: int) -> int:
    arr = [0, 1]
    for i in range(2, n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n]


def fibonacci_3(n: int) -> int:
    a, b = 0, 1
    for i in range(n - 1):
        c = a + b
        a, b = b, c
    return c


def fibonacci_4(n: int) -> int:
    ctx = Context(prec=60)
    sqrt_5 = Decimal(sqrt(5))
    phi = Decimal(1 + sqrt_5)
    psi = Decimal(1 - sqrt_5)
    return int((ctx.power(phi, Decimal(n)) - ctx.power(psi, Decimal(n)))/(2**n * sqrt_5))


def fibonacci_5(n: int, cache={}) -> int:
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci_5(n-1, cache) + fibonacci_5(n-2, cache)
    return cache[n]


def fibonacci_6(n: int) -> int:
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)
    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1],
         [1, 0]]
    for i in range(2, n+1):
        multiply(F, M)


array_of_ns = [5010, 6310, 7940, 10000, 12590, 15850, 19950, 25120, 31620, 39810, 50120, 63100, 79430, 100000, 125890, 158490]
array_of_ns_recursive = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
array_of_ns_memorisation = [50, 128, 196, 212, 254, 298, 324, 344, 378, 399, 414, 786, 1000, 1254, 1408, 1692]
time_array_plot = []
print("   ", end=" ")
for number in array_of_ns_memorisation:
    print(f'{number: >7}', end=" ")
print()
for n in range(3):
    time_array = []
    print(f'{n: ^3}', end=" ")
    for i in array_of_ns_memorisation:
        time_start = time.time()
        fib = fibonacci_5(i)
        time_end = time.time()
        elapsed_time = time_end - time_start
        time_array.append(round(elapsed_time, 4))
        if n == 0:
            time_array_plot = time_array
    for element in time_array:
        print(f'{element: >7}', end=" ")
    print()

plt.plot(array_of_ns_memorisation, time_array_plot, marker='o')
plt.title("Memoization Method")
plt.xlabel("n-th Fibonacci term")
plt.ylabel("Time (s)")
plt.show()