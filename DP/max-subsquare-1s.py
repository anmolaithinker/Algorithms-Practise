import math

def maxSubsquare(matrix):

    rows = len(matrix)
    cols = rows
    s = [[0 for j in range(rows)]for x in range(cols)]
    for i in range(rows):
        s[i][0] = matrix[i][0]

    for i in range(cols):
        s[0][i] = matrix[0][i]

    for i in range(rows):
        for j in range(cols):
            if(matrix[i][j] == 1):
                s[i][j] = min(s[i-1][j] , s[i-1][j-1] , s[i][j-1]) + 1
            elif(matrix[i][j] == 0):
                s[i][j] = 0

    ma = -math.inf
    for i in range(rows):
        m = max(s[i])
        if(m>ma):
            ma = m

    print ("Final Ans : " + str(ma))


matrix = [
    [1,0,0,0],
    [1,1,1,1],
    [1,1,1,0],
    [1,1,1,0]
]

maxSubsquare(matrix)