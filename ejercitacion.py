animal = 0
sexo = 0
perros = 0
gatos = 0
conejos = 0
sexoperros = 0
sexoconejos = 0
cantidadanimal = 0
porgato = 0

while animal != -1:
    animal = int(input("Ingrese el tipo de animal; 1 - perro, 2 - gato, 3 - conejo "))
    sexo = int(input("Ingrese el sexo;  1 para macho, 2 para hembra "))
    if animal == 1:
        perros = perros + 1

    if animal == 2:
        gatos = gatos + 1

    if animal == 3:
        conejos= conejos + 1

    cantidadanimal = perros + gatos + conejos

    if animal == 1 and sexo == 2:
        sexoperros = sexoperros + 1
        
    if animal == 3 and sexo == 1:
        sexoconejos = sexoconejos + 1
        
    porgato = (gatos*100)/cantidadanimal

print("El porcentaje de gatos es ", porgato)
print("La cantidad de perras hembras tratadas fueron ", sexoperros )
print("La cantidad de animales tratados fueron: ", cantidadanimal)
print("La cantidad de conejos machos es ", sexoconejos)


