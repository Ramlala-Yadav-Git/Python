# range(start,stop,stepsize)
# range() function is used to generate a sequence of integers starting from 0 by default,
# and increments by 1 by default, till j-1.

# Syntax :-
# range(start,stop,stepsize)
# Start - Starting position. If don't gie then it's 0
# Stop - Ending position. The range of integers one elemnt prior to stop. If stop is j
# then it will stop at exact j-1
# Stepsize - Increament by stepsize. If we do not mention it, its's 1
a = range(10)
print(a[1])  # 0 se 9 tak chalega
print(range(1, 10))  # 1 se 9 tak chalega
print(range(1, 10, 2))  # 1 ,3,5,7,9 (i,j,k) i, i+k, i+2k -----
