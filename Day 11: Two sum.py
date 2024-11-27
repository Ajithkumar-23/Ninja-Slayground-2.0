def read(n: int, book: [int], target: int) -> str:
    s = set()
    for p in book:
        c = target - p
        if c in s:
            return "YES"
        s.add(p)
    return "NO"
