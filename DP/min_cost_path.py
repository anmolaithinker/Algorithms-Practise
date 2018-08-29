

def minCostPath(matrix):
    rows = len(matrix)
    cols = rows

    s = [[0 for _ in range(cols)]for _ in range(rows)]

    s[0][0] = matrix[0][0]
    for i in range(1,rows):
        s[i][0] = s[i-1][0]+matrix[i][0]

    for i in range(1,cols):
        s[0][i] = s[0][i-1] + matrix[0][i]

    for i in range(1,rows):
        for j in range(1,cols):
            s[i][j] = min(s[i-1][j] , s[i-1][j-1] , s[i][j-1]) + matrix[i][j]

    print("Ans is :" + str(s[rows-1][cols-1]))


matrix = [
    [1,2,3],
    [4,8,2],
    [1,5,3]
]

minCostPath(matrix)