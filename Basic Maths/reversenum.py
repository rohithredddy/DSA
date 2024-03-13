'''You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading zeroes. Return the resulting reversed number.

Example 1:

Input: 200
Output: 2
Explanation: By reversing the digts of
number, number will change into 2.'''

def reverse_digit(n):
	  rev=0
		while n>0:
		    digit=n%10
		    rev=rev*10+digit
		    n//=10
		return rev
reverse_digit(123)
