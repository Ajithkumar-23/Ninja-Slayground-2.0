def upperBound(arr: [int], x: int, n: int) -> int:
    low, high = 0, n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1      
    return ans
