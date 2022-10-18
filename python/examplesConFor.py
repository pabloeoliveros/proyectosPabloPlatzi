                                            #INTERROGATORIO con for

# def personal():
#     entrada = int(input("""
#         Hola, ¿què desea?
#             1. Ver sus id's.
#             2. Solamente ver sus seriales de id.
#             3. Pasaba a molestar un rato...
#     """))

#     identificadores = {
#         "pablo": "010203",
#         "samuel": "010204",
#         "victoria": "010205"
#     }

#     if entrada == 1:
#         for nombres in identificadores.items():
#             print (nombres)

#     elif entrada ==2:
#         for seriales in identificadores.values():
#             print (seriales)

#     elif entrada ==3:
#         print("Estamos trabajando, por favor dejenos continuar...")

#     else:
#         print("No le entendemos...")
#         personal()


# print(personal())






                                                #CALENDARIO con for


def calendario():
    primeraMitad = {
            1 : 'enero',
            2 : "febrero",
            3 : 'marzo',
            4 : "abril",
            5 : 'mayo',
            6 : "junio",
    }
    segundaMitad = {
        7 : 'julio',
        8 : "agosto",
        9 : 'septiembre',
        10 : "octubre",
        11 : 'noviembre',
        12 : "diciembre"
            
    }

    saludoAfable = int(input("¿Quieres ver los meses desde enero o desde junio? (1 o 2): "))

    for meses in primeraMitad.items():
        if saludoAfable ==1:
            print(meses)
        elif saludoAfable ==2:
            for meses2 in segundaMitad.items():
                print(meses2)
            break


print(calendario())





