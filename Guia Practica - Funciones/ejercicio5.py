#1. Crea una variable global llamada nombre_empresa y muéstrala dentro de una función.

global nombre_empresa

def showName():
    global nombre_empresa
    nombre_empresa = "SIGSO"
    print(nombre_empresa)
    
showName()

#2. Crea una función con una variable local llamada total. Intenta utilizarla fuera de la función, observa el error y explícalo.
def calculateTotal():
    total = 100
    print(total)

calculateTotal()
# print(total) #Esto causará un error porque "total" es una variable local y no está definida fuera de la función, para arreglarlo, se podría utilizar la palabra clave "global" y declararla como una variable global.

#3. Crea un contador global y modifícalo desde una función mediante global.
counter = 0

def addCounter():
    global counter
    counter += 1

print(counter)  # Imprime 0
addCounter()    # Añade 1 al contador
print(counter)  # Imprime 1

