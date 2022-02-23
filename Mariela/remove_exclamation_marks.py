# https://www.codewars.com/kata/57a0885cbb9944e24c00008e/train/python
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
def remove_exclamation_marks(s):
    return s.replace('!', '')


string = "Hello World!"
string_1 = "Hi! Hello!"
string_2 = "Oh, no!!!"
print(remove_exclamation_marks(string))
print(remove_exclamation_marks(string_1))
print(remove_exclamation_marks(string_2))