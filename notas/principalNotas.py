#Leer n cantidad de nota decir si es aprendizaje inicial, fundamental, sastifactorio y avanzado, mostrar todas las notas
import aritmeticaNotas as arit

print("Bienvenido al sistema de categorizacion de notas")

arit.readNotes()

print("")
print("La cantidad de notas ingresadas fueron:", arit.showSize())
print("Las notas ingresadas fueron: ", arit.showNotes())
