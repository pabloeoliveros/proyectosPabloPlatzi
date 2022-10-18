def elecciones():
    
    def practica():                                   #5832F0
        coloca1 = int(input("""
        En cuanto a tiempo de estudio, ¿cuánto le dedicas?
        1. 5 a 30 min (por día)
        2. 1 a 2 horas (por día): 
        
        """))
        if coloca1 ==1 or 2:
            respuesta1 = str(coloca1)
            

        coloca2 = int(input("""
        En cuanto a tiempo de ocio, ¿cuánto le dedicas?
        1. 5 a 30 min (por día)
        2. 1 a 2 horas (por día): 
        
        """))
        if coloca2 ==1 or 2:
            respuesta2 = str(coloca2)
            

        coloca3 = int(input("""
        En cuanto a energia, ¿cuán enérgico te sientes?
        1. algo de energía (por día)
        2. sólo duro medio día (por día): 
        
        """))
        if coloca3 ==1 or 2:
            respuesta3 = str(coloca3)
            
        respuestas = (respuesta1 + respuesta2 + respuesta3)
        

        resultados = {
        'FATAL': 'BLA BLA BLA',                                             #111
        'MAL': 'Estàs MAL hermano, toma en cuenta lo siguiente:',            #122 #112 #212
        'BIEN': 'Estàs BIEN, recuerda: ',                                    #121 #221
        'EXCELENTE':'Estàs EXCELENTE, sigue asì!'                           #222

        }

        # for diagnòsticos in resultados.values():
        while 1==1:
            if respuestas == '111':
                print(resultados['FATAL'])
                break

            elif respuestas == '122' or respuestas == '112' or respuestas == '212':
                print(resultados['MAL'])
                break
            elif respuestas == '121' or respuestas == '221':
                print(resultados['BIEN'])
                break
            elif respuestas == '222':
                print(resultados['EXCELENTE'])
                break


    print(practica())

print(elecciones())
        
        
