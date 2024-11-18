from math import *
from collections import *
from sys import *
from os import *

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
n = int(input().strip())
result = fibonacci(n)
print(result)
