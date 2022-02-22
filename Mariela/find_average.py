# Write a function which calculates the average of the numbers in a given list.
#
# Note: Empty arrays should return 0.

def find_average(numbers):
    # your code here
    return sum(numbers) / len(numbers)


number_1 = [1, 2, 3]
print(find_average(number_1))