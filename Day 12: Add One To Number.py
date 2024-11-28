def addOneToNumber(arr):
    n = len(arr)
    c = 1
    for i in range(n - 1, -1, -1):
        if c == 0:
            break
        d = arr[i] + c
        if d < 10:
            arr[i] = d
            c = 0
        else:
            arr[i] = 0
            c = 1
    if c == 1:
        arr.insert(0, 1)
    while len(arr) > 1 and arr[0] == 0:
        arr.pop(0)
    return arr
