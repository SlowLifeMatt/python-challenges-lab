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

# largestthat([1, 2, 3, 4, 0])  # returns 4
# largestthat([10, 4, 2, 231, 91, 54])  # returns 231

# 3. Write a function named occurancesthat takes two string arguments as input and counts the number of occurances of the second string inside the first string.

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








