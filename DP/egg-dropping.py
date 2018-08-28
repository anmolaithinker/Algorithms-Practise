
import math

def eggDrop(num_eggs , num_floors):

    # egg floor
    eggFloor = [[0 for i in range(num_floors+1)] for x in range(num_eggs+1)]

    for i in range(num_eggs):
        eggFloor[i][0] = 0
        eggFloor[i][1] = 1

    for i in range(num_floors):
        eggFloor[1][i] = i

    for i in range(2,num_eggs+1):
        for j in range(2,num_floors+1):
            eggFloor[i][j] = math.inf
            for k in range(1,j):
                res = max(eggFloor[i-1][k-1],eggFloor[i][j-k])
                if(res<eggFloor[i][j]):
                    eggFloor[i][j] = res+1

    return eggFloor[num_eggs][num_floors]


num_eggs = int(input())
num_floors = int(input())
print("Ans is : " + str(eggDrop(num_eggs,num_floors)))