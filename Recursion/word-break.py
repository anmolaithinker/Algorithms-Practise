

def inMap(str):
    l = ['i', 'like', 'sam', 'sung', 'samsung' , 'mobile' , 'ice' ,
         'cream' , 'icecream' , 'man' , 'go' , 'mango' ]
    for i in l:
        if i==str:
            return True
    return False


def printList(ans):
    for i in ans:
        print(i,end=" ")

def isSegmented(input,startIndex,ans):

    if(len(input) == 0):
        printList(ans)
        return True

    for i in range(1,len(input)+1):
        custString = input[startIndex:startIndex + i]
        remainString = input[startIndex+i : len(input)+1]
        ans.append(custString)
        if(inMap(custString) and isSegmented(remainString , startIndex,ans)):
            return True
        ans.pop()

    return False



inputString = input()

ans = []

if(isSegmented(inputString,0,ans)):
    print('Yes')
else:
    print('No')