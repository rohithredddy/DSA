
def insertionSort(arr):
    for i in range(0,len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1 
    return arr
arr = [10,0,2,5,8]
print(insertionSort(arr))


#time complexity for avg and worst O(N^2)


# best case is O(N)
