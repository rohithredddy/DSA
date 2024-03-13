'''Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.
For example:
'N' = 5.
The divisors of 5 are 1, 5.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
10
Sample Output 1 :
1 2 5 10
Explanation of Sample Input 1:
The divisors of 10 are 1,2,5,10.'''

############ ---------- BRUTE FORCE --------- ##########
def printDivisors(n):
    for i in range(1,n+1):     # Time Complexity: O(n), because the loop has to run from 1 to n always.
        if n%i==0:             # Space Complexity: O(1), we are not using any extra space.
            print(i,end=" ")
printDivisors(36)

############ ----------- OPTIMAL APPROACH ------- ##########
def printDivisors(n):
    for i in range(1, int(n**0.5)+1):
            if n % i == 0:                     #Time Complexity: O(sqrt(n)), because every time the loop runs only sqrt(n) times.
                print(i, end=" ")              # Space Complexity: O(1), we are not using any extra space
                if i != n/i:
                    print(int(n/i), end=" ")
