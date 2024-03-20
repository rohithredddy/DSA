def NToOne(i,n):
    if i<1:
        return
    print(i)
    NToOne(i-1,n)
n=int(input())
NToOne(n,n)

# this program prints n to 1 numbers using recursion 

# it takes O(n)
