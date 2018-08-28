import math

def eggDrop(num_eggs , num_floors):

    if(num_floors == 0 or num_floors ==1):
        return num_floors

    if(num_eggs == 1):
        return num_floors

    result = math.inf
    for i in range(1,num_floors+1):

        # agar anda foota
        foota = eggDrop(num_eggs-1,i-1)

        # agar anda nhi foota
        nhi_foota = eggDrop(num_eggs,num_floors-i)

        #max of both
        max_trial = max(foota,nhi_foota)

        if max_trial < result:
            result = max_trial

    return result+1



num_eggs = int(input())
num_floors = int(input())

res = eggDrop(num_eggs , num_floors)
print("Ans is  : " + str(res))