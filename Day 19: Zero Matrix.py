def zeroMatrix(matrix, n, m):
    r = any(matrix[0][j] == 0 for j in range(m))
    c = any(matrix[i][0] == 0 for i in range(n))
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, n):
        if matrix[i][0] == 0:
            for j in range(m):
                matrix[i][j] = 0
    for j in range(1, m):
        if matrix[0][j] == 0:
            for i in range(n):
                matrix[i][j] = 0
    if r:
        for j in range(m):
            matrix[0][j] = 0
    if c:
        for i in range(n):
            matrix[i][0] = 0
    return matrix
