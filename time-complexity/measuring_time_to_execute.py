# This approach is not used in industry because, this varries depending on the system hardware i.e. corei7 > corei5
# If you keep the logic same, but change the process from for to while loop, time efficency will change

import time

start = time.time()
for i in range(1, 101):
    print(i)

# i = 1
# while i<101:
#     print(i)
#     i+=1

print(time.time() -start)

#if small things change so time efficency between "time and input" cant be measured for an algorithm with this technique

