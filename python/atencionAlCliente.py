productos = """
    1. Caja clap
    2. Combo para el desayuno
    3. Combo para el almuerzo
    4. Combo premium para la cena

    ¿Te gusta alguno? ¡Sòlo pìdelo!

"""
eleccion = int(input(productos))

preciobajo = "25 bolivares "
precioalto = "50 bolivares "
modalidad1 = " Paypal, èste es el nùmero..."
modalidad2 = " Cash, el cambio le serà devuelto en persona"



def opciones(modificable):
    print("Es un total de " + modificable)
    print ("su modalidad de pago es " + modalidad1 + " o tambièn en" + modalidad2)
if eleccion ==1:
    opciones(preciobajo)

elif eleccion ==2:
     opciones(preciobajo)

elif eleccion ==3:
     opciones(precioalto)

elif eleccion ==4:
     opciones(precioalto)

