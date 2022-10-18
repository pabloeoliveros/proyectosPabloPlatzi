                #menu de nuestro bar INVESTIGA Y APRENDE ESTO



class Bar:

    menu = {

        'vino': 4,
        'cerveza': 3,
        'refresco':2,
        'pollo':10,
        'carne':15,
        'ensalada':12,
        'postre':6

    }


                #funcion de inicializacion con una lista vacio
    def __init__(self):
        self.total = 0
        self.objetos = []


                #funcion que añade objetos a la lista vacia e incrementar el total
    def add(self, objeto):
        self.objetos.append(objeto)     #metodo para agregar cosas a la lista: append
        self.total += self.menu[objeto]     #forma de actualizar el total


                #funcion para mostrar el total de todo
    def print_factura(self,impuesto,servicio):
        impuesto = (impuesto/100)*self.total
        servicio = (servicio/100)*self.total
        total = self.total + impuesto + servicio

        for objeto in self.objetos:
            print(f'(objeto:20) ${self.menu[objeto]}')
        
        print(f'{"Total"} ${total:.2f}')