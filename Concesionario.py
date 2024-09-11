class Carro:
    def __init__(self,modelo,precio):
        self.modelo=modelo
        self.precio=precio
        self.disponibles=True
    def ventas(self):
        if self.disponibles:
            self.disponibles=False
            print(f"El vehiculo {self.modelo} ha sido vendido")
        else:
            print(f"El vehiculo {self.modelo} no esta disponible")
    def devolver_carro(self):
        self.disponibles=True
        print(f"El vehiculo {self.modelo} ha sido devuelto")
class User:
    def __init__(self,name,user_id):
        self.name=name
        self.user_id=user_id
        self.carros_comprado=[]
    def carro_comprado(self,carro):
        if carro.disponibles:
            carro.ventas()
            self.carros_comprado.append(carro)
        else:
            print(f"El vehiculo {carro.modelo} noi esta disponible")
    def devolver_carro(self,carro):
        if carro in self.carros_comprado:
            carro.devolver_carro()
            self.carros_comprado.remove(carro)
        else:
            print(f"El vehiculo {carro.modelo} no esta en la lista de vendidos")
class Concesionario:
    def __init__(self):
        self.carros=[]
        self.users=[]
    def add_carro(self,carro):
        self.carros.append(carro)
        print(f"El vehiculo {carro.modelo} ha sido agregado")
    def register_user(self,user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")
    def carros_disponibles(self):
        print("Vehiculos disponibles: ")
        for carro in self.carros:
            if carro.disponibles:
                print(f"{carro.modelo} por ${carro.precio}")
#Crear los Carros
carro1=Carro("Camaro","3500")
carro2=Carro("mustan gt 4","7500")
#Crear usario
user1=User("Lucas","0001")
#Crear lista de carros
concesionario=Concesionario()
concesionario.add_carro(carro1)
concesionario.add_carro(carro2)
concesionario.register_user(user1)
#Mostrar carros
concesionario.carros_disponibles()
#realisar venta
user1.carro_comprado(carro1)
#Mostrar carros
concesionario.carros_disponibles()
#Devolucion Carro
user1.devolver_carro(carro1)
#Mostrar carros
concesionario.carros_disponibles()