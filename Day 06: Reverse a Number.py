def reverseNumber(n: int) -> int:
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n //= 10 
    return rev
