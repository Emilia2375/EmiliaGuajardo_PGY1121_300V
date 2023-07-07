#Codigo
import numpy as np

#Bienvenida al programa
print("*"*58)
print("¡Venta de entradas concierto Michael Jam! No te lo pierdas")
print("by: Creativos.cl")
print("*"*58)

#Listas y arange's

#rut_asistentes = ["por hacer"]
menu = ["Comprar entradas","Mostrar ubicaciones disponibles","Ver listado de asistentes", "Mostrar ganacias totales", "Salir"]
asientos = np.arange(1,101).reshape(10,10)

#Def/enumerate
def construir(x):
    for a,b in enumerate(x):
        print(f"{a+1}. {b}")
        choice = input("elige una opcion: \n")
        return choice

def analizar(x):
        global asientos
        if x == "1":
            print("¡Valor entradas!")
            print("La zona platinum tiene un valor de $120.000 pesos. (Asientos del 1 al 20)")
            print("La zona Gold tiene un valor de $80.000 pesos. (Asientos del 21 al 50)")
            print("La zona Silver tiene un valor de $50.000 pesos. (Asientos del 51 al 100)")
            print("Ingrese los asientos que desea comprar(recuerde el maximo de 3 asientos por rut): \n")
#Ubicaciones disponibles
        elif x == "2":
            print("Estos son los asientos disponibles: \n")
            print(str(asientos).replace("["," ").replace("]", " ").replace(" 0", " X"))
            
#Listado de asientos
        elif x == "3":
            pass
#Ganacias totales
        elif x == "4":
            pass
#opcion salir
        elif x == "5":
            print("Hasta luego!")
            print("esto fue una venta dirigida por 'Creativos.cl'")
            print("Programa realizado por Emilia Guajardo, fecha: 6/7/2023")

#control de error        
        else:
            print("Ingrse una opcion valida porfavor\n")

#no se pq no me muestra todo, lloro



while True:
    analizar(construir(menu))
