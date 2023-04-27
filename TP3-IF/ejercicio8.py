dia = int(input("Ingrese un día "))
mes = int(input("Ingrese un mes "))
anio = int(input("Ingrese un año "))

if dia >= 1 and dia <= 31 and mes >= 1 and mes <= 12 and anio >=1900 and anio <= 2023:
    print("La fecha: ", dia, "/", mes, "/", anio, "es valida") 
else:
    print("La fecha ingresada no es valida")