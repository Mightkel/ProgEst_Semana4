import aritmetica as arit

def menu():
    print("Bienvenido a Mi Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    op = int(input("Digite el # de la opcion deseada: "))
    return op

def showAdd(num1, num2):
    print(f"La suma de {num1} + {num2} es {arit.add(num1,num2)}")
    
def showSub(num1, num2):
    print(f"La resta de {num1} - {num2} es {arit.sub(num1,num2)}")
    
def showMult(num1, num2):
    print(f"La multiplicacion de {num1} * {num2} es {arit.mult(num1,num2)}")

def showDiv(num1, num2):
    print(f"La division de {num1} / {num2} es {arit.div(num1,num2)}")
    
def readValues():
    num1 = float(input("Digita el primer valor: "))
    num2 = float(input("Digita el segundo valor: "))
    return num1, num2

def chooseOp(op):
    if op == 1:
        num1, num2 = readValues()
        showAdd(num1,num2)
    elif op == 2:
        num1, num2 = readValues()
        showSub(num1,num2)
    elif op == 3:
        num1, num2 = readValues()
        showMult()
    elif op == 4:
        num1, num2 = readValues()
        showMult()
    elif op == 0:
        print("Adios")
        return False
    else:
        print("Opcion invalida...")

def main():
    while True:
        op = menu()
        if op == 0: break
        if op > 0 and op <= 4: chooseOp(op)
        else: print("Opcion invalida")

main()