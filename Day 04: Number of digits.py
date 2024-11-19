import math
def countDigits(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    return math.floor(math.log10(n)) + 1
