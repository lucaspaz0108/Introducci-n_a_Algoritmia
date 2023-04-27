km_de_viaje = int(input("Ingrese su recorrido en km "))
viaje_minimo = 250
recorrido1 = 30
recorrido2= 20

if km_de_viaje < viaje_minimo * recorrido1:
    print("Se cobra ", viaje_minimo, "que es el viaje minimo")
elif km_de_viaje < 10 :
    print("Se cobra ", km_de_viaje * recorrido1)
elif km_de_viaje > 10:
    print("Se cobra ", km_de_viaje * recorrido2)