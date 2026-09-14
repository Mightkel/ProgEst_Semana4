#1. Crea una función que reciba un salario numérico, aumente su parámetro y comprueba si cambió la variable original.

def aumentar_salario(salario):
    salario = salario + 1000
    print("Salario dentro de la función:", salario)
    return salario

salario_original = 2000

aumentar_salario(salario_original)

print("Salario fuera de la función:", salario_original)

#2. Crea una función que reciba una lista de ventas y agregue una nueva venta mediante append().

def agregar_venta(ventas, nueva_venta):
    ventas.append(nueva_venta)
    return ventas

ventas = [100, 200, 300]
print("Ventas antes de la función:", ventas)

agregar_venta(ventas, 400)
print("Ventas después de la función:", ventas)

#3. Explica por qué los dos ejercicios producen comportamientos diferentes.
## En el primer ejercicio, se trata de una variable numerica, que solo tiene un valor y solamente se puede modificar dentro de la función, 
# mientras que en el segundo ejercicio, se trata de una lista, que es un objeto mutable y puede ser modificado dentro de la función. 
# Por lo tanto, el primer ejercicio no cambia la variable original, mientras que el segundo sí.