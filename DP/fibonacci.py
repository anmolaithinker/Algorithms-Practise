

def fib(n):
    res = [0 for x in range(n+1)]
    res[0] = 0
    res[1] = 1
    for i in range(2,n+1):
        res[i] = res[i-1] + res[i-2]
    return res[n]


n = 9
print(fib(n))