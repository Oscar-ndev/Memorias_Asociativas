import tkinter as tk
from collections import deque

# Ventana principal
root = tk.Tk()
root.title("Práctica 2: Juego de las Fichas")
root.geometry("800x600+400+100")
root.resizable(False, False)
root.config(bg="lightblue") 

# Convertir el estado a una lista bidimensional
def convertir_estado_a_matriz(estado):
    return [list(estado[:2]), list(estado[2:])]

# Convertir la matriz de vuelta a cadena
def convertir_matriz_a_estado(matriz):
    return ''.join(matriz[0] + matriz[1])

# Función para mover la ficha 'b' en las 4 direcciones posibles
def mover_ficha(matriz):
    for i in range(2):
        for j in range(2):
            if matriz[i][j] == 'b':
                fila_b, col_b = i, j

    movimientos = []

    if col_b > 0:
        nueva_matriz = [fila[:] for fila in matriz]
        nueva_matriz[fila_b][col_b], nueva_matriz[fila_b][col_b - 1] = nueva_matriz[fila_b][col_b - 1], nueva_matriz[fila_b][col_b]
        movimientos.append(nueva_matriz)

    if col_b < 1:
        nueva_matriz = [fila[:] for fila in matriz]
        nueva_matriz[fila_b][col_b], nueva_matriz[fila_b][col_b + 1] = nueva_matriz[fila_b][col_b + 1], nueva_matriz[fila_b][col_b]
        movimientos.append(nueva_matriz)

    if fila_b > 0:
        nueva_matriz = [fila[:] for fila in matriz]
        nueva_matriz[fila_b][col_b], nueva_matriz[fila_b - 1][col_b] = nueva_matriz[fila_b - 1][col_b], nueva_matriz[fila_b][col_b]
        movimientos.append(nueva_matriz)

    if fila_b < 1:
        nueva_matriz = [fila[:] for fila in matriz]
        nueva_matriz[fila_b][col_b], nueva_matriz[fila_b + 1][col_b] = nueva_matriz[fila_b + 1][col_b], nueva_matriz[fila_b][col_b]
        movimientos.append(nueva_matriz)

    return movimientos

# Búsqueda por Amplitud (recorrido en anchura)
def busqueda_amplitud(estado_inicial, estado_objetivo):
    cola = deque([(convertir_estado_a_matriz(estado_inicial), [estado_inicial])])  # Cola FIFO
    visitados = set()

    text_box.insert(tk.END, "Búsqueda en Amplitud:\n")
    while cola:
        resultado = ', '.join([convertir_matriz_a_estado(e[0]) for e in cola])
        text_box.insert(tk.END, f", {resultado}\n")  # Agregar cada paso al text_box1

        matriz_actual, camino = cola.popleft()
        estado_actual = convertir_matriz_a_estado(matriz_actual)

        if estado_actual == estado_objetivo:
            return camino

        if estado_actual not in visitados:
            visitados.add(estado_actual)

            for nueva_matriz in mover_ficha(matriz_actual):
                nuevo_estado = convertir_matriz_a_estado(nueva_matriz)
                if nuevo_estado not in visitados:
                    cola.append((nueva_matriz, camino + [nuevo_estado]))

    return None

# Búsqueda por Profundidad (recorrido en profundidad)
def busqueda_profundidad(estado_inicial, estado_objetivo):
    pila = [(convertir_estado_a_matriz(estado_inicial), [estado_inicial])]  # Pila LIFO
    visitados = set()
    #print("\nEvolución de la pila durante la búsqueda en profundidad:")
    text_box1.insert(tk.END, "Búsqueda en Profundidad:\n")
    while pila:
        # Imprimir el estado actual de la pila
        resutladopila = ', '.join([convertir_matriz_a_estado(pila[-1][0])] + [convertir_matriz_a_estado(e[0]) for e in pila[:-1]])
        text_box1.insert(tk.END, f", {resutladopila}\n")  # Agregar cada paso al text_box1
        matriz_actual, camino = pila.pop()
        estado_actual = convertir_matriz_a_estado(matriz_actual)

        if estado_actual == estado_objetivo:
            return camino

        if estado_actual not in visitados:
            visitados.add(estado_actual)

            for nueva_matriz in mover_ficha(matriz_actual):  # Exploramos en profundidad
                nuevo_estado = convertir_matriz_a_estado(nueva_matriz)
                if nuevo_estado not in visitados:
                    pila.append((nueva_matriz, camino + [nuevo_estado]))

    return None

# Función principal que ejecuta ambos algoritmos
def resolver_juego(estado_inicial, estado_objetivo):
    solucion_amplitud = busqueda_amplitud(estado_inicial, estado_objetivo)
    solucion_profundidad = busqueda_profundidad(estado_inicial, estado_objetivo)

def validar_un_caracter(entrada):
    return len(entrada) <= 1

def leer_entrys():
    btnJugar.config(state="disabled")
    btnLimpiar.config(state="normal")
    text1 = lblFicha1.get()
    text2 = lblFicha2.get()
    text3 = lblFicha3.get()
    text4 = lblFicha4.get()
    lblFicha1.config(state="disabled")
    lblFicha2.config(state="disabled")
    lblFicha3.config(state="disabled")
    lblFicha4.config(state="disabled")
    estado_inicial = text1+text2+text3+text4
    estado_objetivo = "b312"
    resolver_juego(estado_inicial, estado_objetivo)
    



def Limpiar_Contenido():
    lblFicha1.config(state="normal")
    lblFicha2.config(state="normal")
    lblFicha3.config(state="normal")
    lblFicha4.config(state="normal")
    lblFicha1.delete(0, tk.END)
    lblFicha2.delete(0, tk.END)
    lblFicha3.delete(0, tk.END)
    lblFicha4.delete(0, tk.END)
    text_box.delete(1.0, tk.END)
    text_box1.delete(1.0, tk.END)
    btnJugar.config(state="normal")
    btnLimpiar.config(state="disabled")
    




# Crear un botón
btnJugar = tk.Button(root, text="Jugar", command=leer_entrys, font=("Aptos", 20), bg="blue", fg="white")
btnJugar.pack()

btnLimpiar = tk.Button(root, text="Limpiar", command=Limpiar_Contenido, font=("Aptos", 15), bg="green", fg="white")
btnLimpiar.place(x=690, y=1)
btnLimpiar.config(state="disabled")

lblInitialState = tk.Label(root, text="Estado Inicial", font=("Aptos", 20))
lblInitialState.place(x=15 , y=15)
lblInitialState.config(bg="lightblue")

validacion = root.register(validar_un_caracter)


lblFicha1 = tk.Entry(root, validate="key", width=2, font=("Aptos", 40), validatecommand=(validacion, '%P'))
lblFicha1.place(x=30, y=60)  # Primera fila, primera columna
lblFicha1.config(justify="center")
lblFicha2 = tk.Entry(root, validate="key", width=2, font=("Aptos", 40), validatecommand=(validacion, '%P'))
lblFicha2.place(x=90, y=60)  # Primera fila, segunda columna
lblFicha2.config(justify="center")
lblFicha3 = tk.Entry(root, validate="key", width=2, font=("Aptos", 40), validatecommand=(validacion, '%P'))
lblFicha3.place(x=30, y=125)  # Segunda fila, primera columna
lblFicha3.config(justify="center")
lblFicha4 = tk.Entry(root, validate="key", width=2, font=("Aptos", 40), validatecommand=(validacion, '%P'))
lblFicha4.place(x=90, y=125)  # Segunda fila, segunda columna
lblFicha4.config(justify="center")

lblFinalState = tk.Label(root, text="Estado Final", font=("Aptos", 20))
lblFinalState.place(x=15 , y=350)
lblFinalState.config(bg="lightblue")

lblFicha1f = tk.Entry(root, width=2, font=("Aptos", 40))
lblFicha1f.place(x= 30, y=395)
lblFicha1f.insert(0,'b')
lblFicha1f.config(justify="center", state="disabled")
lblFicha2f = tk.Entry(root, width=2, font=("Aptos", 40))
lblFicha2f.place(x= 90, y=395)
lblFicha2f.insert(0,'3')
lblFicha2f.config(justify="center", state="disabled")
lblFicha3f = tk.Entry(root, width=2, font=("Aptos", 40))
lblFicha3f.place(x= 30, y=460)
lblFicha3f.insert(0,'1')
lblFicha3f.config(justify="center", state="disabled")
lblFicha4f = tk.Entry(root, width=2, font=("Aptos", 40))
lblFicha4f.place(x= 90, y=460)
lblFicha4f.insert(0,'2')
lblFicha4f.config(justify="center", state="disabled")
text_box = tk.Text(root, width=20, height=15, font=("Helvetica", 16))  # Fuente más grande
text_box.place(x=200, y=120)


text_box1 = tk.Text(root, width=22, height=15, font=("Helvetica", 16))  # Fuente más grande
text_box1.place(x=500, y=120)


lblcola = tk.Label(root, text="Cola", font=("Aptos", 20))
lblcola.place(x=300 , y=75)
lblcola.config(bg="lightblue")

lblpila = tk.Label(root, text="Pila", font=("Aptos", 20))
lblpila.place(x=600 , y=75)
lblpila.config(bg="lightblue")




root.mainloop() 
