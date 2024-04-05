hashaa=[0]*26
a=input("enter a string: ")
for i in a:
    hashaa[ord(i)-ord("a")]+=1
    
q= int(input("enter number of quieries:"))
while q>0:
    c=input("enter charcter to count;")
    print(hashaa[ord(c)-ord("a")])
    q-=1

# using hashing

