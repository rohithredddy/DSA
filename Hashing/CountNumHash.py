arr1 = [1, 2, 1, 2, 3, 4, 5, 7, 9, 12]
hasha = [0] * 13                         # Initialize the hash array with zeros
for i in arr1:
    hasha[i] += 1
q = int(input())
while q > 0:                             # Corrected the while loop condition
    number = int(input())
    print(hasha[number])
    q -= 1                                # Decrement q by 1 in each iteration



# counting a number in array that it apperas how many times using HASHING
