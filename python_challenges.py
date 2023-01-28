# 1. Write a function named sum_tothat accepts a single integer, n, and returns the sum of the integers from 1 to n.

num = int(input( "enter a integer: " ))
sum_to=num

for i in range(1, sum_to): 
    sum_to += i
    print(sum_to)

