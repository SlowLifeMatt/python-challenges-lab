# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

# num = int(input( "enter a integer: " ))
# sum_to=num

# for i in range(1, sum_to): 
#     sum_to += i
#     print(sum_to)

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

# ------------------------

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largestNum( list ):
    largest = list[ 0 ]
    for number in list:
        if number > largest:
            largest = number
    return largest
print(largestNum([10, 4, 2, 231, 91, 54]))

# largestNum([1, 2, 3, 4, 0])  # returns 4
# largestNum([10, 4, 2, 231, 91, 54])  # returns 231

# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# Only gave me one letter

# def occurences (stringA, stringB):
#     count = 0
#     for doubleword in stringA:
#         for letter in doubleword:
#             if letter == stringB:
#                 count = count + 1
#     return count # Had this one tab over originally and code returned an incorrect value
# stringA = input("stringA: ")
# stringB = input("stringB: ")

# occurence = occurences(stringA,stringB)

# print(occurence)

#------------

# This method still only gave me one letter

# def occurence (stringA, StringB):
#     count = 0

#     for i in range(len(stringA)):
#         if (stringA[i] == StringB):
#             count = count + 1
#     return count

# stringA = input("stringA: ")
# stringB = input("stringB: ")
# print(occurence(stringA, stringB))

#----------

#Final

# def occurence(stringA, stringB):
#     word = len(stringA)
#     search = len(stringB)
#     count = 0

#     for i in range(search - word + 1):
#         j = 0
#         while(j < word):
#             if(stringB[i + j] != stringA[j]):
#                 break
#             j += 1
#         if (j == word):
#             count += 1
#             j = 0
#     return count 
# stringA = input("stringA: ")
# stringB = input("stringB: ")

# print(occurence(stringB, stringA))

#-----------

#Okay maybe one is my final

stringA = input("stringA: ")
stringB = input("stringB: ")
occurence = 0
for count in range(len(stringA) - len(stringB) + 1):
    if(stringA[count:count+len(stringB)] == stringB):
        occurence += 1
print(occurence)

#---------------

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.

def product(*args):
    total = 1
    for num in args:
        total *= num
    return total
print(product(4, 0.5, 5))

# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0






