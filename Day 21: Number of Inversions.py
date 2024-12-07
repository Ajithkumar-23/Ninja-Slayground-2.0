from typing import List
def numberOfInversions(a: List[int], n: int) -> int:
    def merge_sort_and_count(arr, temp, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        inversions = merge_sort_and_count(arr, temp, left, mid)
        inversions += merge_sort_and_count(arr, temp, mid + 1, right)
        inversions += merge_and_count(arr, temp, left, mid, right)
        return inversions
    def merge_and_count(arr, temp, left, mid, right):
        i, j, k = left, mid + 1, left
        inversions = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inversions += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = temp[i]
        return inversions
    temp = [0] * n
    return merge_sort_and_count(a, temp, 0, n - 1)
