# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
# Note: input will never be an empty string

def fake_bin(x):
    lista = ""
    for i in x:
        if int(i) < 5:
            lista = lista + "0"
        elif int(i) >= 5:
            lista = lista + "1"
    return lista


lista1 = "555"
print(fake_bin(lista1))
