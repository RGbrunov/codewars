# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]

def maps(a1):
    result = []
    for i in a1:
        result.append(i + i)
    return result


a = [1, 2, 3]
print(maps(a))
