
# eleccion = int(input("""
# Por favor pick-a-chu jaja ok no :D ...escoje un numero por favor: (1,2,3)
# """)) 


# def opciones(frase1):
#     print("Gracias por tu aporte, este es nuestro sms para ti: ")
#     oracion = print(frase1)
#     return oracion


# if eleccion == 1:
#     opciones("Yo soy Tyson en el 96'")

# elif eleccion == 2:
#     opciones("Y Cobe posteao' tirando el Fade away")

# elif eleccion == 3:
#     opciones("Kbron yo le dije a mi armero")

# else:
#     opciones("Que el AKPistol los parte como la pierna e` McGregor")



                                               #Comparaciòn de EDADES y NOMBRES


# def edades():
#     saludo1 = int(input("Hola, Me llamo Pablo ¿Podrìas decirme cuàl es tu edad?: "))
#     nombre1 = input("¿como te llamas?: ")
#     respuesta1 = saludo1

#     saludo2 = int(input("Hola, Me llamo Pablo ¿Podrìas decirme cuàl es tu edad?: "))
#     nombre2 = input("¿como te llamas?: ")
#     respuesta2 = saludo2

#     while respuesta1 > respuesta2:
#         print(nombre1 + " es mayor que " + nombre2)
#         break

#     while respuesta2 > respuesta1:
#         print(nombre2 + " es mayor que " + nombre1)
#         break

# print(edades())







                                        #FUNCIONES

# def run():
#     LIMITE = 1000

#     contador = 0
#     potenciaA2 = 2 ** contador
#     while potenciaA2 < LIMITE:
#         print('2 elevado a ' + str(contador)+
#             ' es igual a: ' + str(potenciaA2))
#         contador +=1
#         potenciaA2 = 2 ** contador

# print(run)

# if __name__ == '__main__':
#     run()

# def billeteraA():
#     cifra = int(input('¡Hola! Ingresa un nùmero menor a 5 por favor: '))
#     FULL = 21

#     while cifra < FULL:
#         numeroIngresado = str(cifra)
#         if cifra < FULL:
#             print('tienes un total de ' + numeroIngresado + ' criptos disponibles')
#             cifra +=1
#         if cifra == FULL:
           
#             print("""
            
#             Has llegado al limite, gracias por tu tiempo :)
            
#             """)

# billeteraA()
# print(billeteraA)




    


# def suma():   #F0AF80                          #A
#     def resta(c,d):                         #B
#         primeraresta = c - d                        #C
#         return primeraresta                         #C

#     return resta                            #B

# totaltotal = suma()(5, 2)           #AByC
# print(totaltotal)



                                                #EL PODER DE LAS LISTAS
# lista = ["ma ", "me ", "mi ", "mo " ]

# lista.append("mu ")
# lista.pop(4)



# def comidas1():
#     comidasYprecios = ["papa" , 1, "cilantro", 2, "perejil", 3]
#     cambio = comidasYprecios[0]
#     print(cambio)


# def comidas2():
#     comidasYprecios = ["papa" , 1, "cilantro", 2, "perejil", 3]
#     cambio = comidasYprecios[2]
#     print(cambio)
    

# def bienvenida():
#     inicio = int(input('escoje si 1 o 2: '))
#     if inicio == 1:
#         print(comidas1())
#     if inicio == 2:
#         print(comidas2())

# print(bienvenida())











# def ferreteria (puerta1, puerta2, manija1, manija2):    #CREE una funcion principal (ferreteria) donde dì 2 opciones al usuario 
#                                                         #y una subfuncion para cualquiera de las opciones que tome (despedida)

#     saludo = int(input("""
#         Hola, bienvenido a nuestra ferreteria, disponemos de puertas y llaves para 
#         la comodidad de su casa, ¿desea ver alguna?:
#             1. Si, comencemos con esa puerta de Granito
#             2. Seguro, llevame a la de "Madera Rojiza"
#             3. Vuelvo luego, ¡muchas gracias!
#     """))


#     puertas = {                             #une ambos diccionarios para que san uno solo e invocalos con FOR.items
#         'puerta1': puerta1,
#         'puerta2': puerta2,
#     }
#     llaves = {
#         'llave1': manija1,
#         'llave2': manija2,
#     }
    

#     def despedida():
#             pregunta = int(input("""¿Desea pagar?: 
#             1. Si
#             2. No, vuelvo luego ¡gracias!
#             R: """))

#             if pregunta ==1:
#                 print("Esto es suyo, gracias por su compra, lo esperamos pronto!")
#             elif pregunta ==2:
#                 print("Gracias por su tiempo, ¡lo esperamos pronto!")

            
    
#     while saludo == 1:
        
#         print(puertas['puerta1'],"con", llaves['llave1'])
#         print("valor de" + "20$" + "(sin instalaciòn incluida)")
#         despedida()
#         break
    
#     while saludo ==2:
        
#         print(puertas['puerta2'],"con", llaves['llave2'])
#         print("valor de" + "25$" + "(sin instalaciòn incluida)")
#         despedida()
#         break

#     while saludo ==3:
#         print("Agradecemos tu visita, vuelve pronto")
#         break


# print(ferreteria('Granito incluido', 'Madera rojiza', 
#                 'doble cerrojo', 'manilla anticizalla'))


                                    #MODULO 6  MÈTODOS: Superpoder para la variable


# sentencia = "el come coco"
# words = sentencia.split()

# longitudPalabra = [len(palabra) for palabra in words if palabra != "el"]
# print(words)
# print(longitudPalabra)

# soloUnaFraseMas = "Me gusta programar"
# modificacion = soloUnaFraseMas.split()

# otraFraseMas = "asereje"
# modificacion2 = otraFraseMas.capitalize()
# # print (modificacion2)

# escriboBienMiCodigo = "BUENAESA"
# modificacion3 = escriboBienMiCodigo.casefold()
# print(modificacion3)

# aprendoDelPasado = "no mires atras pablo"
# modificacion4 = aprendoDelPasado.center(4, '*')
# # print(modificacion4)


# import random


# frankSinatra = [1, 2, 3, 4, 5, 6]
# random.shuffle(frankSinatra)

# print(frankSinatra)

                                                #LISTCOMPREHENSIONS 

# frutas = ['manzana', 'banana', 'parchita' ,'melon', 'kiwi']
# nuevaLista = []

# for fruta in frutas:
#     if 'a' in fruta: #si hay alguna "a" en cada fruta: anexalo a nuevaLista"
#         nuevaLista.append(fruta)

# print(nuevaLista)


#con list compreh. serìa asì:

frutas = ['manzana', 'banana', 'parchita' ,'melon', 'kiwi']

nuevaLista = [fruta for fruta in frutas if "a" in fruta]
print(nuevaLista)