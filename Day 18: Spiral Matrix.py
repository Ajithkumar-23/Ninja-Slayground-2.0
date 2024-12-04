from typing import List
def spiralMatrix(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    res = []
    t, b = 0, len(matrix) - 1
    l, r = 0, len(matrix[0]) - 1
    while t <= b and l <= r:
        res.extend(matrix[t][l:r + 1])
        t += 1
        for i in range(t, b + 1):
            res.append(matrix[i][r])
        r -= 1
        if t <= b:
            res.extend(matrix[b][l:r + 1][::-1])
            b -= 1
        if l <= r:
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1    
    return res
