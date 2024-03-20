def oneToN(i,n):
    if i>n:
        return
    print(i)
    oneToN(i+1,n)
n=int(input())
oneToN(1,n)

# TC : O(N)
