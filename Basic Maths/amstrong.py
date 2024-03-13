'''Problem statement
You are given an integer 'n'.
Return 'true' if 'n' is an Armstrong number, and 'false' otherwise.
Note:
An Armstrong number is a number (with 'k' digits) such that the sum of its digits raised to 'kth' power is equal to the number itself.
For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.
Example:
Input: 'n' = 1634
Output: true
Explanation:
1634 is an Armstrong number, as 1^4 + 6^4 + 3^4 + 4^4 = 1634'''

def amstrong(n):
    org=n
    temp=n
    sum1=0
    count=len(str(n))  #suitable for all test cases
    # while temp!=0:
    #     count+=0       not suitable for some test cases
    #     temp//=10
    while n!=0:
        digit=n%10
        sum1+=digit**count      # Time Complexity: O(n) where n is the number of digits since we need to traverse every digit and add digits raised to power no. of digits to sum.
        n//=10                  # Space Complexity: O(1) since no extra space is required
    if sum1==org:
        print("true")
    else:
        print("false")
a=int(input())
amstrong(a)
