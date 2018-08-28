
def isSafe(maze,row,col,n):
    for i in range(col):
        if(maze[row][i] == 'Q'):
            return False
    i = row-1
    j = col-1
    while(i>=0 and j>=0):
        if(maze[i][j] == 'Q'):
            return False
        i = i-1
        j = j-1

    for i in range(row):
        if(maze[i][col] == 'Q'):
            return False

    return True


def printMaze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print (str(maze[i][j]) + ' ' , end = '')
        print (' ')

def PutQueens(maze,col,n):
    print ('Column :' + str(col))
    if(col>=n):
        print('-'*100)
        printMaze(maze)
        print ('-'*100)
        return True
    for i in range(n):
        if(isSafe(maze,i,col,n)):
            maze[i][col] = 'Q'
            if(PutQueens(maze,col+1,n)):
                return True
            maze[i][col] = 0
    return False


board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

print (PutQueens(board,0,4))