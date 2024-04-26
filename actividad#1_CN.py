class Cuenta:
    def __init__(self):
        self.titular = ""
        self.cantidad = float(100)
    def getCantidad(self):
        return self.cantidad
    def getTitualr(self):
        return self.titular
    def setCantidad(self, numero, cantidad):
        if cantidad < 1:
            print("La cantidad de inicio de cuenta colocada es invalida")
            return
        if numero == 1:
            self.cantidad -= cantidad
            if self.cantidad < 0:
                print("Tu balance esta en negativo!")
        elif numero == 2:
            self.cantidad += cantidad
        elif numero == 3:
            self.cantidad = cantidad
        else:
            print("Opcion no valida")
    def setTitular(self, nombre):
        self.titular = nombre
    
nueva =Cuenta()
while nueva.titular == "":
    nueva.titular = input("(Obligatorio) Nombre del Titular: ")
print("La cantidad default de la cuenta es de 100$")
a = int(input("Desea colocar una cantidad inicial a la cuenta? 1 = si, 2 = no: "))
if a == 1:
        cantidad1 = float(input("Cual es la cantidad inicial de la cuenta?: "))
        nueva.setCantidad(3, cantidad1)
        print("La cantidad inicial ahora es de:")
        print(nueva.getCantidad())
loops = "s"
while loops == "s":
    b = int(input("Que desea hacer? 1. Retirar, 2. Depositar, 3. Cancelar Operacion: "))
    if b == 3:
        loops = "n"
        c = int(input("Deseas ver el estado de tu cuenta? 1 = si, 2 = no: "))
        if c == 1:
            print("La cantidad de tu cuenta es de:")
            print(nueva.getCantidad())
        print("Gracias por venir!")
    elif b == 2:
        cantidad1 = float(input("Cual es la cantidad que desea depositar?: "))
        nueva.setCantidad(b, cantidad1)
    elif b == 1:
        cantidad1 = float(input("Cual es la cantidad que desea retirar?: "))
        nueva.setCantidad(b, cantidad1)

