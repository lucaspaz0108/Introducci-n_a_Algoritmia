nota1 = int(input("Ingrese su primer nota "))
nota2 = int(input("Ingrese su segunda nota "))
promedio = nota1 + nota2 / 2

if promedio >= 7:
    print("El alumno promocinó")
elif promedio >= 4:
    print("El alumno aprobó")
else:
    print("El alumno desaprobó")