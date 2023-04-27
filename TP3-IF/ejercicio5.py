costobasico = 500
valorpagina = 3.20
numpag = int(input("Ingrese el número de hojas "))
total_libro = costobasico + valorpagina * numpag

if numpag <= 300:
    print("El valor total del libro es ", total_libro)
elif numpag > 300:
    print("El valor total del libro es ", total_libro + 200)
elif numpag > 600:
    print("El valor total del libro es ", total_libro + 336)


