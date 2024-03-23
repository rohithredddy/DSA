def fibonaccin(n):
    if n<=1:
        return n
    return fibonaccin(n-1)+fibonaccin(n-2)
n=int(input())
print(fibonaccin(n))
