arr=[13,46,24,52,20,9]
for i in range(0,len(arr)):
    mini=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[mini]:
            mini=j
    arr[mini],arr[i]=arr[i],arr[mini]
print(arr)



# time complexity is O(n^2)
