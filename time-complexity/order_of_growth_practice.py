# Question 1:

L = [1,2,3,4,5] 

sum = 0
for i in L:
    sum = sum+1
    # sum = sum+i # prints the sum
print(sum) #prints the number of values in a list

product = 1
for i in L:
    product = product*i
print(product)

'''
O(n)
Loop 1: O(n)
Loop 2: O(n)

for full Loop 1 + Loop 2 = 2O(n)
Remove multiplicant constonant so full =  O(n)
Time Complexity =  Linear
'''

# Question 2:


for i in L:
    for j in L:
        print('({},{})'.format(i,j)) #breaks the array L in pair so (1,1), (1,2), ... (3,2) 
"""
O(n) = O(n)^2

Time Complexity =  Quadratic
"""


# Question 4: Linear Search -> order of N, array double time double:


#Question 5:

#code converts integer into string:

#Brilliant piece of code
def intTostr(i):
    digits= "0123456789"

    if i == 0:
        return "0"
    result = ""
    while i > 0:
        result = digits[i%10] + result
        i = i//10
    return result

print(intTostr(123))
print(type(intTostr(123))) 

# O(n) = 
"""
input:                      123 1230 12300
resulting in loop rotation: 3  4     5

Time Complexity =  Log
"""

#__________________________________________________________________

# Question 6:


# Question 7: Binary Search -> time complexity = Lograthmic (code in search engine sorting)

# Question 8:

for i in range(0, len(L)):
    for j in range(i+1,len(L)):
        print("({},{}))".format(L[i],L[j]))

# loop 1 running n times,
# loop 2 running n-1 times 
# O(n)^2


#Problem 9:

A = [1,2,3,4]
B = [2,3,4,5,6]

for i in A:
    for j in B:
        if i < j:
            print("({},{}))".format(i,j))

# Time complexity = O(ab)

#Problem 10:
#Reverse array

L = [1,2,3,4,5]

for i in range(0,len(L)//2):
    other = len(L) -i -1
    temp = L[i]
    L[i] = L[other]
    L[other] = temp

print(L)


#Probelem 11
# Recursion

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n*factorial(n-1)
    
print(factorial(5))

# 10 factorials so 10 functions called, so linear O(n)

#depends on the functions call (search for more examples!)