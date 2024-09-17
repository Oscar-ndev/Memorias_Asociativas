""" Práctica 1
Castañeda Nuñez Nephtali
López Victorino Oscar Abiud """

animales = ['hamster', 'perro', 'gato', 'pez', 'vaca', 'caballo', 'oso', 'jirafa', 'mono', 'aguila', 'tiburon']

preguntas = [
    "¿Es un animal doméstico?",   # 0
    "¿Es un mamífero?",           # 1
    "¿Es un animal acuático?",    # 2
    "¿Es un animal carnívoro?",   # 3
    "¿Puede volar?",              # 4
    "¿Es un animal de granja?",   # 5
    "¿Tiene manchas?",            # 6
    "¿Es un animal pequeño?",     # 7
    "¿Es cuadrúpedo?",            # 8
    "¿Tiene un rabo largo?",      # 9
    "¿Puede trepar árboles?"      # 10
]

respuestas = {
    'hamster':  [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    'perro':    [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
    'gato':     [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    'pez':      [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    'vaca':     [0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    'caballo':  [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    'oso':      [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    'jirafa':   [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    'mono':     [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    'aguila':   [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    'tiburon':  [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
}

def jugar():
    print("Estos son los animales que tengo en mi base de datos:")
    for x in animales:
        print(x)
    print('Adivinare el animal que elijas, si respondes las siguientes preguntas: ')
    posible_respuesta = animales.copy()
    lista_respuestas_animal = []

    for i, pregunta in enumerate(preguntas):
        print(pregunta)
        while True:
            respuesta_usuario = input("Responde con 'si' o 'no': ").lower()
            if respuesta_usuario in ['si', 'no']:
                break  
            else:
                print("Respuesta no válida. Responde con 'si' o 'no'.")

        comparacion_binaria = 1 if respuesta_usuario == 'si' else 0

        posible_respuesta = [animal for animal in posible_respuesta if respuestas[animal][i] == comparacion_binaria]

        if len(posible_respuesta) == 1:
            print(f"¡El animal es {posible_respuesta[0]}!")
            break  

        if not posible_respuesta:
            print("No hay animales que coincidan con las respuestas proporcionadas.\n¿Te gustaría agregar el animal en el que estás pensando a mi base de datos?")
            while True:
                respuesta_agregar_animal = input("Responde con 'si' o 'no': ").lower()
                if respuesta_agregar_animal == "si":
                    nombre_animal = input('Dime el nombre del animal: ')
                    for x in preguntas:
                        print(x)
                        while True:
                            repuesta_agregadas = input("Responde con 'si' o 'no': ").lower()
                            if repuesta_agregadas in ['si', 'no']:
                                break  
                            else:
                                print("Respuesta no válida. Responde con 'si' o 'no'.")    
                        lista_respuestas_animal.append(1) if repuesta_agregadas == 'si' else lista_respuestas_animal.append(0)
                    respuestas[nombre_animal] = lista_respuestas_animal
                    animales.append(nombre_animal)
                    break  
                elif respuesta_agregar_animal == "no":
                    break
                else:
                    print("Respuesta no válida. Responde con 'si' o 'no'.")
            break
    else:
        print(f"No se pudo determinar con certeza el animal. Posibles opciones: {posible_respuesta}")

while True:
    jugar() 

    while True:
        jugar_nuevamente = input("¿Quieres jugar de nuevo? Responde con 'si' o 'no': ").lower()
        if jugar_nuevamente == 'no':
            print("¡Gracias por jugar! Hasta luego.")
            exit() 
        elif jugar_nuevamente == 'si':
            break  
        else:
            print("Respuesta no válida. Responde con 'si' o 'no'.")