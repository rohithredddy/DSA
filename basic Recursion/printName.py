def printName(i,n):
    if i>n:
        return
    print("rohith")
    printName(i+1,n)
n=int(input())
printName(1,n)
