# objetivo = int(input('coloca un numero: '))
# BASE = 1
# LIMITE = 11

# while BASE + objetivo < LIMITE:            #AQUI se produce una sumatoria entre las 2 constantes para una comparac. con LIMITE
#     BASE +=1                                #aquì se explica que ocurre si es menor a LIMITE

#     if objetivo == BASE:                                    #AQUÌ van diversas condiciones si BASE no es igual a limite
#         print(str(objetivo) + f' es igual a ' + str(BASE))
#     elif BASE + objetivo == LIMITE:
#         print(f'El numero ' + str(BASE) + ' es igual a 10')
#     else:
#         print(str (objetivo) + f' no es igual a ' + str(BASE))

#                                                 #haz un relog con zona horaria (caracas-New York-Madrid)

















# print(busquedaBinaria())




                                                        #FUNCIONES CON VARIEDAD DE PARÀMETROS. 
                    # #con keywords y por defecto
# def operaciones(primer, segundo, numero=1):
#     primer = 2
#     segundo = 3

#     seleccion = int(input("selecciona 1 o 2: "))
#     if seleccion == 1 :
#         numero = True
#         if numero ==True:
#             restaPositiva = float(segundo - primer)
#             print(restaPositiva)

#     if seleccion == 2:
#         numero = False
#         if numero ==False:
#             restaNegativa = int(primer - segundo)
#             print(restaNegativa)

# print(operaciones(2,3))


                    #PARAM. OBLIGADO

# def palabras(nombre):
#     oraciòn ='me llamo ' + nombre
#     return oraciòn
    
# print(palabras('pablo'))

                    #PARAM. PREDEFINIDO
# def palabras(nombre, apellido = 'Oliveros'): #la razon por la cual "OLIVEROS" No està invocada debajo 
#                                               #es porque fue invocada al inicio

#     hola = (int(input('¿1 o 2?: ')))
#     holaNuevo= str(hola)

#     for respuesta in holaNuevo:
#         if respuesta == '1':
#             oracion1='me llamo ' + nombre + apellido
#             return oracion1
#         elif respuesta == '2':
#             apellido = 'Gutierrez'
#             oracion2 = 'Oliveros no es mi apellido, sino: ' + apellido
#             return oracion2

# print(palabras('Pablo'))


                    #PARAM. VARIADO !!!!!!!!!!!!!!!!!!!!!
# def nombres(*args):
    
#     entrada = int(input('1 o 2: '))
#     entradaNueva = str(entrada)

#     for respuesta in entradaNueva:
#         if respuesta == '1':
#             oracion = 'Me llamo ' + args
#             return oracion

# print(nombres('Pablo'))
        # elif respuesta == '2':
        #     nombre= 'Julio'
        #     apellido='De la Fuente'
        #     oracion = 'Yo no me llamo Pablo, sino' + nombre + apellido + ', y tengo: ' + args + 'años'




# def factorial(n):

#     if n ==1:
#         return 1
#     else:
#         return n * factorial(n -1)          #¿porquè fue necesario colocar "factorial(n -1)" aqui, 
#                                             #en vez de colocar solamente (n -1)?
        

# n = int(input('Escribe un numero: '))
# print(factorial(n))