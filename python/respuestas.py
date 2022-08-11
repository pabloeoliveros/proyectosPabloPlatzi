bienvenida = str(input("Hola, ¿còmo estàs?: "))

if bienvenida == "Bien":
    print("Gracias por tu buen trato")

elif bienvenida == "Mal":
    print("Wow, ¿còmo te ayudo?")

else:
    print("Bueno, anda a freir monos")

        #corrige error de impresion con "Bien" y "Mal", No deberìa arrojar la misma respuesta
        #error CORREGIDO: 1. cuida los 4 espacios bajo cada if/elif/else
                        # 2. si el bloque de codigo tiene mas opciones, va con elif, sino: con else.