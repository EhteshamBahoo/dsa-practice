def c_to_f(c):
    return c*9.0/5 + 32 # 3 operations

def mysum(x):
    total = 0 # 1 operation
    for i in range(x):  # 1 operation
        total += 1  # 2 operations
    return total

# 1 operation happening outside and 3 happening inside loop so formula: 1 + 3x (x=input) x = 10, so 1 + 3(10) = 31.

# This appraoach improves and doesn't depend on hardware as it counts operations
# It also provides with a mathmatical relation between time and input

# But time changes when implementation is changed

