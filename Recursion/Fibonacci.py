

def fibinaccinthNum(n):
    if(n<=1):
        return n
    return fibinaccinthNum(n-1) + fibinaccinthNum(n-2)

print(fibinaccinthNum(9))