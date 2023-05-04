number = int(input("Ingrese un numero "))
inverted_number = 0
while number > 0:
    inverted_number = inverted_number * 10 + number % 10
    number = number // 10
print(inverted_number)