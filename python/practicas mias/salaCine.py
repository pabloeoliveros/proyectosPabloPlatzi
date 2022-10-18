def taquilla():
    peliculas = """A continuaciòn una lista de nuestras recientes peliculas (2$ por entrada):
        1. La Momia
        2. Una noche en el museo
        3. Rapidos y Furiosos: Reto Tokio
    
    Por favor escoje con 1,2 o 3:
    """
        
    def opciones():
        opciones2 = int(input("""¿Desea ver nuestra lista de combos disponibles?
                1. ¡Seguro!
                2. No, llevame a caja
                3. Gracias, vuelvo luego
                : """))
        for elecciones in range (1,3):
                if opciones2 ==1:
                    combos()
                    break
                elif opciones2 ==2:
                    caja()
                    break
                elif opciones2 ==3:
                    print('Gracias por visitarnos, ¡recuerda seguirnos en las redes @cinescareros en Fakestagram y Cringer tambien!')
                    return elecciones
        
        
    peliculas = int(input(peliculas))
    while peliculas ==1 or peliculas ==2 or peliculas==3:
        resultadoTaquilla = peliculas
        opciones()


        def combos(comida1,bebida1,comida2,bebida2,comida3,bebida3):          #conecta esto con las opciones correspond...
                        presentacionMenu ='Actualmente, en cines Careros disponemos de las siguientes opciones: '
                        menu={
                            'plato1' : comida1 + 'con '+ bebida1,
                            'plato2' : comida2 + 'con ' + bebida2,
                            'plato3' : comida3 + 'con ' + bebida3,
                        }
                        print (presentacionMenu)
                        print(menu['plato1'])
                        print(menu['plato2'])
                        print(menu['plato3'])
                        
                        combos('2 hamburguesas ', '1 vaso de pepsi ',
                        'SuperPatacon (para 3 personas) ', '1 1/2 litro de 7up ',
                        '1 servicio de Tequeños fritos ','2 lt de Frescolita ' )
        escoje = int(input("""Por favor, escoje una opciòn:
                            plato 1: 2 hamburguesas con 1 vaso de pepsi (por 5$) 
                            plato 2: SuperPatacon (para 3 personas) con 1 1/2 litro de 7up (por 8.99$)
                            plato 3: 1 servicio de Tequeños fritos con 2 lt de Frescolita (por 7$)"""))
        if escoje ==1 or escoje ==2 or escoje==3:
                    eleccionDelMenu = str(escoje)
                    adelante = int(input("""¿Desea pagar?
                            1. Si
                            2. Gracias, vuelvo luego
                            : """))
                    for adelante in range (1,3):
                        if adelante ==1:
                                caja()
                                break
                        elif adelante ==2:
                                print('Gracias por visitarnos, ¡recuerda seguirnos en las redes @cinescareros en Fakestagram y Cringer tambien!')
                                break
                        else:
                                print('Gracias por visitarnos, ¡recuerda seguirnos en las redes @cinescareros en Fakestagram y Cringer tambien!')


    def caja():
        if resultadoTaquilla ==1:
            resultadoTaquilla = 'La Momia (2$)'
        elif resultadoTaquilla ==2:
            resultadoTaquilla = 'Una noche en el museo (2$)'
        elif resultadoTaquilla ==3:
            resultadoTaquilla = 'Rapidos y Furiosos: Reto Tokio (2$)'

        sumatoriaTotal = f'Usted ha escojido { resultadoTaquilla} y las siguientes comidas: {eleccionDelMenu}'
        print(sumatoriaTotal)



                
    return resultadoTaquilla



 

bienvenida = """
Bienvenido a Cines Careros, ¿en què te puedo ayudar? Por favor, selecciona una opciòn (1,2,3)

1. Quiero ver una pelicula


#NoWayHolmes #LosMasTaquilleros 
: """

bienvenida = int(input(bienvenida))

if bienvenida ==1:
    print(taquilla())
else: 
    print('Gracias por visitarnos, ¡recuerda seguirnos en las redes @cinescareros en Fakestagram y Cringer tambien!')

print(taquilla())