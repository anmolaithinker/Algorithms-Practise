
def isSafe(adj_matrix,color,current_vertex,n,color_arr):
    for i in range(n):
        if(adj_matrix[current_vertex][i] and color_arr[i] == color):
            return False
    return True


def PrintColor(color_Arr):
    for i in range(len(color_Arr)):
        print(color_Arr[i] , end=" ")

def assignColorsUtils(adjMatrix,n,num_colors,visited,current_vertex,color_arr):
    if(current_vertex == n):
        PrintColor(color_arr)
        return True

    visited[current_vertex] = 1
    for i in range(num_colors):
        if(isSafe(adj_matrix,i,current_vertex,n,color_arr)):
            color_arr[current_vertex] = i
            if(assignColorsUtils(adjMatrix,n,num_colors,visited,current_vertex+1,color_arr)):
                return True
            color_arr[current_vertex] = -1
    return False


def assignColors(adjMatrix , n , num_colors):
    visited = []
    color_arr = []
    for i in range(n):
        visited.append(0)
        color_arr.append(-1)
    if(assignColorsUtils(adjMatrix,n,num_colors,visited,0,color_arr)):
        print ('Yes')
    else:
        print ('No')


# 4 vertex
adj_matrix = [
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
]

assignColors(adj_matrix,4,3)