'''Given an integer, check if it is prime or not. Print true if number is prime, print false otherwise.
Sample Input 1 :
7
Sample Output 1 :
 true
Sample Input 2 :
15
Sample Output 2 :
 false'''

##############---------BRUTE FORCE-------------############
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

########---------------OPTIMAL APPROACH-------------########
def checkPrime(n):
  # Special case for 2
  if n <= 1:
    return False
  elif n <= 3:
    return True
  # Only check for odd divisors since even numbers are not prime (except 2)
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:                                           #Time Complexity: O(√n)
      return False                                           #Space Complexity: O(1)
  return True

a = int(input())
ans = checkPrime(a)
if ans:
  print("true")
else:
  print("false")

