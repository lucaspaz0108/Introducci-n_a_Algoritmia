persona1 = int(input("Ingrese el dinero invertido "))
persona2 = int(input("Ingrese el dinero invertido "))
persona3 = int(input("Ingrese el dinero invertido "))

inversion_total = persona1+persona2+persona3

inversionp1 = (persona1 / inversion_total) * 100
inversionp2 = (persona2 / inversion_total) * 100
inversionp3 = (persona3 / inversion_total) * 100

print("Porcentaje de inversión de la persona 1 es ", inversionp1, "%")
print("Porcentaje de inversión de la persona 2 es ", inversionp2, "%")
print("Porcentaje de inversión de la persona 3 es ", inversionp3, "%")
