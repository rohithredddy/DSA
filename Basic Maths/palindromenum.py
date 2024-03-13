'''Problem statement
Check whether a given number ’n’ is a palindrome number.
Note :
Palindrome numbers are the numbers that don't change when reversed.
You don’t need to print anything. Just implement the given function.
Example:
Input: 'n' = 51415
Output: true
Explanation: On reversing, 51415 gives 51415.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
1032
Sample Output 1 :
false
Explanation Of Sample Input 1:
1032, on being reversed, gives 2301, which is a totally different number.'''

def palindrome(n):    
    rev=0
    temp=n
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    if temp==rev:
        print("true")
    else:
        print("false")
n=int(input())
palindrome(n)
