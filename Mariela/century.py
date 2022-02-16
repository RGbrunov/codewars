# El primer siglo abarca desde el año 1 hasta el año 100 inclusive, el segundo siglo - desde el año 101 hasta el año 200 inclusive, etc.
# Task
# Given a year, return the century it is in.
#
# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
def century(year):
    result = int(year / 100)
    if year % 100 > 0:
        result = result + 1
    return result


lista1 = 1705
print(century(lista1))
lista2 = 1900
print(century(lista2))
lista3 = 1601
print(century(lista3))
lista4 = 2000
print(century(lista4))
