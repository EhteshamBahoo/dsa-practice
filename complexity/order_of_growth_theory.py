# What do we want?
# We want to evaluate the algorithm
# We want to evaluate the scalabilty 
# We want to evaluate in terms of input size

# Important Constant:
# Best case : result found earliest and fastest
# Average case: result found in middle
# Worst case: result found at last, slowest

# When designing an algorithm the focus should be on the perfeormance on Worst Case!

# #Order of Growth :
# 1. evaluate progam's efficency when input is very big
# 2. express the growth of program's run time as input size grows (need a relationship between input and time)
# 3. want to put an upperbound on growth- as tight as possible
# 4. dont need to be precise: "order of" not "exact" growth
# 5. look at the largest factors in the runtime (like focusing on nested loop over single loop)

#the Big(O) notation

def fact_inner(x):
    answer = 1 # 1 operation
    while n>1: # 1 operation
        answer *= n # 2 operation
        n-=1 # 2 operation
    return answer

# equation 1+5n
# O(n)
#1. remove added in constants
#2. remove multiplicant constants 
#cancel 1 and 5, so the relationship between input and time is linear.



# Formaula understanding practice:


'''
n^2 + 2n + 2
n^2 = nested loop
2n = operations inside loop
2 = operations outside loop

n^2 + 2n + 2 in Big(O)
1. n^2 + 2n + 2
2. n^2 + 2n
3. n^2 + n (focus on larger factor nested loop>loop)
4. n^2 Answer!

The relation is quadratic
'''
#2
"""
n^2 + 10000n + 3^10000
n^2 + 10000n
n^2 + n
"""
#3
"""
log(n) + n + 4
log(n) + n
n 
"""

#4
"""
2n^30 + 3^n
3^n
"""


#Note these are all for very big numbers


#List of possible relations:

'''
1. constant
2. Linear
3. Quadratic
4. Lograthmic
5. n log n
6. exponential
'''

#on a graph!
x = "input"
y = "time"

# Constant: e.g. Index item extraction is a constant time operation, as it doesn't use the len(), rather it adds upon the allocated memory(Search more!)
# Linear: e.g. Linear Search, searching an item in an array, the larger the array is, the longer the time it takes
# Quadratic: e.g. if you double the input, it will take 4x time. If you have nested loops that quadratic i.e. bubble sort etc.
# Lograthmic: e.g. if input increases 10x times, then the time will only increase by 1 e.g (it is the best after constant)
'''
input: 10 100 1000 (multiplies)
time:  1  2   3  (add)
for example binary search
'''

#n log n: sorting examples, merge sort for example

#exponential: the opposite of log the worst! 
 