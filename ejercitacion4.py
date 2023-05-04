"""Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válida una edad entre 0 y 100)."""

edad, cont18,contmas18,edadtotales, edadpromediomenores,cantidadgente,ciclo, edadpromediomayores,edadmen, edadmay = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

while edad != -1:
    edad = int(input("Ingrese su edad "))
    if edad >= 0 and edad <= 100:
        if edad < 18:
            cont18 = cont18 + 1
            edadmen = edadmen + edad
        if edad >= 18:
            contmas18 = contmas18 + 1
            edadmay = edadmay + edad
    
cantidadgente = cont18 + contmas18
edadpromediomenores= edadmen / cont18
edadpromediomayores = edadmay / contmas18
print("La cantidad de menores de 18 es ", cont18)
print("La cantidad de mayores de 18 es ", contmas18)
print("La edad promedio de los menores de 18 es ", edadpromediomenores)
print("La edad promedio de los mayores de 18 es ", edadpromediomayores)