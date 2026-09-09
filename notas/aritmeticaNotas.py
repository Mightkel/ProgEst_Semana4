#Funciones para leer la nota e identificar su categoria
notes = []
categories = []
def addNote(note):
    notes.append(note)
    return 0

def showSize():
    return len(notes)

def showNotes():
    return notes

def readNotes():
    while True:
        try:
            note = float(input("Ingrese su nota: "))
            if note > 0 and note < 100:
                addNote(note)
                if note > 0 and note < 70:
                    print("Aprendizaje Inicial")
                    categories.append("Aprendizaje Inicial")
                elif note > 69 and note < 80:
                    print("Aprendizaje Fundamental")
                    categories.append("Aprendizaje Fundamental")
                elif note > 79 and note < 90:
                    print("Aprendizaje Sastifactorio")
                    categories.append("Aprendizaje Sastifactorio")
                elif note > 89 and note < 101:
                    print("Aprendizaje Avanzado")
                    categories.append("Aprendizaje Avanzado")
            else:
                print("La nota no puede ser negativa o superior a 100")
            answer = input("Desea ingresar otra nota? ( S - N ): ")
            if answer.upper() != "S":
                break
            print("")
        except ValueError:
            print("Debe ingresar un numero")
            
