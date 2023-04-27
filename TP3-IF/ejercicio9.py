sueldo_basico = int(input("Ingrese su sueldo básico "))
antiguedad = int(input("Ingrese su antiguedad en años "))
estado_civil = int(input("Ingrese su estado civil: 1 si es soltero, 2 si es casado "))
aumento_soltero = (sueldo_basico * 5) / 100
aumento_casado = (sueldo_basico * 7) / 100
sueldo_ant = 0

if estado_civil == 1:
    sueldo_ant = antiguedad * aumento_soltero
elif estado_civil == 2:
    sueldo_ant= antiguedad * aumento_casado

sueldo_total = sueldo_ant + sueldo_basico

jubilacion = (sueldo_total * 11) / 100
obra_social = (sueldo_total * 3) / 100
sindicato = (sueldo_total * 3) / 100

print("el sueldo total es: ", sueldo_total - jubilacion - obra_social - sindicato)
