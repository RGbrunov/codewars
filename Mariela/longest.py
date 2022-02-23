# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
#
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    a3 = list(dict.fromkeys(sorted(a1 + a2)))  #La función del diccionario de Python fromkeys () se utiliza para crear un nuevo diccionario
    return "".join(a3)


lista1 = "aretheyhere"
lista2 = "yestheyarehere"
print(longest(lista1, lista2))
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))