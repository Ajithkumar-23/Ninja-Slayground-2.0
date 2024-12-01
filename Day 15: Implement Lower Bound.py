from typing import List
def lowerBound(arr: List[int], n: int, x: int) -> int:
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid   
    return left
