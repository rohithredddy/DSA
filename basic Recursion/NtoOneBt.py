def NtoOneBt(i,n):
    if i>n:
        return
    NtoOneBt(i+1,n)
    print(i)
n=int(input())
NtoOneBt(1,n)
