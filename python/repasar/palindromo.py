                                        #1er BLOQUE DE CODIGO, Pero es el ultimo por no tener el entrypoint
def palindromo(palabra):
    palabra = palabra.replace('', '')
    palabra = palabra.lower()           #una vez hagas una funcion, es importante dejar 2 lineas libres entre cada funcion
    palabra_invertida = palabra[::-1]
    
    if palabra == palabra_invertida:
        return True
    else:
        return False

                                        #2do BLOQUE DE CODIGO, Pero es el primero en correr por estar en el entrypoint
def run():
    palabra = input('escribe una palabra: ')
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

                                        #3do BLOQUE DE CODIGO, Pero es el primero en ser visto por Python
if __name__== '__main__': #toda lo que dice "main" y està en amarillo, es el entrypoint de python, a partir de allì, 
    run()                 #comienza a correr el programa