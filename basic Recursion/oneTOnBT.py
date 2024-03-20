def oneToNBT(i,n):
    if i<1:
        return
    oneToNBT(i-1,n)
    print(i)
n=int(input())
oneToNBT(n,n)

# printing 1 to n using recursion but with back tracking
