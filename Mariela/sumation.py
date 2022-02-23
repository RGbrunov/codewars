# https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python
# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
#
# For example:
#
# summation(2) -> 3
# 1 + 2
#
# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
def summation(num):
    my_sum = 0
    i = 0
    while i <= num:
        my_sum = my_sum + i
        i += 1
    return my_sum


numero = 2
print(summation(numero))
numero_1 = 8
print(summation(numero_1))