def calcGCD(n: int, m: int) -> int:
    while m:
        n, m = m, n % m
    return n
