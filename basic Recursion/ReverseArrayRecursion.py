a=[41,52,86,96,85,45,-85,45,-54]
def RevereseArrayRecursion(l,r):
    if l>=r:
        return
    a[l],a[r]=a[r],a[l]
    RevereseArrayRecursion(l+1,r-1)
RevereseArrayRecursion(0,len(a)-1)
print(a)
