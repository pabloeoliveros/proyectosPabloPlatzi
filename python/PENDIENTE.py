miDiccionario = {
        1: 'Crepusculo',
        2 : 'Twilight',
        3 : 'Moon',
}

print(miDiccionario.items())
entrada = (input('Bienvenido a nuestra libreria, ¿te gusta algun libro? escoje con 1, 2 o 3: '))


for ingreso in entrada:
        if ingreso =='1':
                print(miDiccionario.keys[1])
        elif ingreso =='2':
                pass
        elif ingreso =='3':
                pass





def tuplas():
        tupla3 = (7,8,9)
        cajaMayor = opcion1,opcion2,opcion3 = tupla3

        entrada = int(input('Favor ingresa in numero del 1 al 3: '))
        entrada = str(entrada)
        
        for respuesta in entrada:
                if respuesta == 1:
                        return cajaMayor[0]

                elif respuesta == 2:
                        return cajaMayor[1]

                elif respuesta == 3:
                       return cajaMayor[2]
        


def recorte():
    accion = 10
    

    for i in range(0,11):
        while i == 10:
            accion // 2
        if accion >=3:
            accion -=1
        elif accion == 2 or accion == 2.5:
            print(f'convertiste {str(10)} + en {str(accion)} ')

        return accion

print(recorte())



                                #haz 12 ejercicios de List attachment (3por dia)
def operacion():
        digitos = list(range(10))
        ingresa = input('ingresa un numero: ')

        for numeros in digitos:
                if ingresa <'10':
                        ingresa = int(ingresa)
                        ingresa = [ingresa+1 for ingresa in digitos]
        return numeros
        

print(operacion())