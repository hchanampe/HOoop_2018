class Fila(object):
    """Clase base de fila"""

    def __init__(self):
         """constructor de la clase Fila """
         self.enfila=0
         self.fila=[]

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        if cliente.categoria == 'preferencial':
            self.fila.append(cliente)
            self.enfila+=1
        else:
            print("El cliente no es preferencial")

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        if maxenfila<self.enfila:
            filanueva = FilaPreferencial()
            
    
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila+=1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
        

class cliente(object):
     """clase cliente """
     def __init__(self,dni):
         """ constructor de la clase cliente """
         self.dni=dni
         self.categoria=None
     def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria=categoria
     def getCategoria(self):
        return self.categoria
     def __str__(self):
         return "DNI:"+str(self.dni)+" - Categoria:"+self.categoria
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    
    customer = cliente(30311931)
    customer.modificarcategoria("preferencial")
    fila = FilaPreferencial()
    fila.insertar(customer)
    
    print(fila.enfila)
    
