# 1. Write a function named sum_tothat accepts a single integer, n, and returns the sum of the integers from 1 to n.

# num = int(input( "enter a integer: " ))
# sum_to=num

# for i in range(1, sum_to): 
#     sum_to += i
#     print(sum_to)

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

# ------------------------

# 2. Write a function named largestthat takes a list of numbers as an argument and returns the largest number in that list.

def largestthat( list ):
    largest = list[ 0 ]
    for number in list:
        if number > largest:
            largest = number
    return largest
print(largestthat([10, 4, 2, 231, 91, 54]))

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

