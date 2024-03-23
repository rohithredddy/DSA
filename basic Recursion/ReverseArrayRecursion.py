#two pointer approach
a=[41,52,86,96,85,45,-85,45,-54]
def RevereseArrayRecursion(l,r):
    if l>=r:
        return
    a[l],a[r]=a[r],a[l]
    RevereseArrayRecursion(l+1,r-1)
RevereseArrayRecursion(0,len(a)-1)
print(a)

# one pointer approach 

a=[1,2,3,4,5]
def RevereseArrayRecursion1(i):
    if i>=len(a)//2:
        return
    a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
    RevereseArrayRecursion1(i+1)
RevereseArrayRecursion1(0)
print(a)
