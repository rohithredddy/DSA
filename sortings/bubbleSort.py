
arr=[9, 13, 20, 24, 46, 52]
didswap=0
for i in range(len(arr)-1,0,-1):
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            didswap+=1
    if didswap==0:
        break
print(arr)

# bubble sort tc for worst and avg cases is O(n^2)
# for best case when array is already sorted then O(N)



