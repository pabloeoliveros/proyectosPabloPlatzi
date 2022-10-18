#primero definimos la cantidad, estimaciòn del dolar y su numeraciòn
dolar = input("Porfavor ingrese su cantidad de dolares: ")
dolar = float(dolar)
valor_dolar = 6
dolar = round(dolar, 2)

#luego definimos a què es igual el bolivar y como se estima en bolivares
bolivar = dolar * valor_dolar
bolivar =str(bolivar)
print("Tienes " + bolivar + " bolivares en total")
