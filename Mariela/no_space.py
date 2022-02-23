# https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/python
# Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(" ", "")


string_1 = '8 j 8   mBliB8g  imjB8B8  jl  B'
print(no_space(string_1))
string_2 = '8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'
print(no_space(string_2))