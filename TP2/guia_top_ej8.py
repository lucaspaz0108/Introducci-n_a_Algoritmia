medida = float(input("Ingrese una medida en metros "))

medidacm = medida * 100

medidapul = float(medidacm / 2.54)

medidapie = medidapul / 12

medidayar = medidapie / 3

print("Su medida en centímetros es: ", medidacm)
print("Su medida en pulgadas es: ", medidapul)
print("Su medida en pies es: ", medidapie)
print("Su medida en yardas es: ", medidayar)