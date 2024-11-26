from typing import List
from collections import Counter
def getFrequencies(v: List[int]) -> List[int]:
    freq = Counter(v)
    high = min((n for n, f in freq.items() if f == max(freq.values())))
    low_elems = [n for n, f in freq.items() if f == min(freq.values())]
    low = min(low_elems)
    return [high, low]
