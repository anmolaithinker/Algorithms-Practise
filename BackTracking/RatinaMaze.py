
def isSafe(maze,x,y,n):
    if(x >= n or y>=n):
        return False
    elif(maze[x][y]!=1):
        return False
    return True

def checkIfTrue(maze,x,y,n):
    if(x == n-1 and y == n-1):
        return True
    if(isSafe(maze,x,y,n)):
        if(checkIfTrue(maze,x+1,y,n)):
            return True
        if(checkIfTrue(maze,x,y+1,n)):
            return True
    return False


# maze
maze = [
    [1,0,0,1],
    [1,1,0,0],
    [1,0,0,1],
    [1,1,1,1]
]

if(checkIfTrue(maze,0,0,4)):
    print ('Yes it is possible')
else:
    print ('No')