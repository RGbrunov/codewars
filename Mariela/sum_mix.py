# https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.

def sum_mix(arr):
    total = 0
    for valor in arr:
        total += int(valor)

    return total


test = [1, 8, 5, "5"]
print(sum_mix(test))