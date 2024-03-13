'''Given an integer, check if it is prime or not. Print true if number is prime, print false otherwise.
Sample Input 1 :
7
Sample Output 1 :
 true
Sample Input 2 :
15
Sample Output 2 :
 false'''

def checkPrime(n):
    count=0
    for i in range(1,n+1):        # Time Complexity: O(n)
        if n%i==0:                # Space Complexity: O(1)
            count+=1
    if count==2:
        print("true")
    else:
        print("false")
a=int(input())
checkPrime(a)
