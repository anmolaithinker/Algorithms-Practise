
def maxDivide(n,d):
    while(n%d == 0):
         n = n/d
    return n

def isUgly(n):
    n = maxDivide(n,2)
    n = maxDivide(n,3)
    n = maxDivide(n,5)
    if n == 1:
        return True
    return False

def uglyCount(n):
    count = 1
    i = 1
    while(count<n):
        i = i+1
        if(isUgly(i)):
            count = count+1

    print(i)


n = 7
uglyCount(n)