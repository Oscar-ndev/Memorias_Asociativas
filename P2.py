import tkinter as tk
from collections import deque


# Función que genera los posibles movimientos de fichas
def obtener_movimientos(posicion):
    movimientos = []
    fila, columna = posicion
    if fila > 0:  # Movimiento hacia arriba
        movimientos.append((fila - 1, columna))
    if fila < 1:  # Movimiento hacia abajo
        movimientos.append((fila + 1, columna))
    if columna > 0:  # Movimiento hacia la izquierda
        movimientos.append((fila, columna - 1))
    if columna < 1:  # Movimiento hacia la derecha
        movimientos.append((fila, columna + 1))
    return movimientos

# Función para intercambiar el espacio vacío con una ficha
def intercambiar(tablero, pos_vacia, nueva_pos):
    nuevo_tablero = [fila[:] for fila in tablero]  # Copiar el tablero
    fila_vacia, col_vacia = pos_vacia
    nueva_fila, nueva_col = nueva_pos
    nuevo_tablero[fila_vacia][col_vacia], nuevo_tablero[nueva_fila][nueva_col] = nuevo_tablero[nueva_fila][nueva_col], nuevo_tablero[fila_vacia][col_vacia]
    return nuevo_tablero

# Función de búsqueda en amplitud (Cola)
def busqueda_amplitud(estado_inicial, estado_final):
    cola = deque([(estado_inicial, encontrar_posicion_vacia(estado_inicial), [])])
    visitados = set()

    while cola:
        tablero, pos_vacia, camino = cola.popleft()
        if tablero == estado_final:
            return camino  # Devuelve el camino (secuencia de movimientos)
        
        visitados.add(tuple(map(tuple, tablero)))  # Marcar como visitado
        
        for movimiento in obtener_movimientos(pos_vacia):
            nuevo_tablero = intercambiar(tablero, pos_vacia, movimiento)
            if tuple(map(tuple, nuevo_tablero)) not in visitados:
                cola.append((nuevo_tablero, movimiento, camino + [nuevo_tablero]))
    
    return None  # No hay solución

# Función de búsqueda en profundidad (Pila)
def busqueda_profundidad(estado_inicial, estado_final):
    pila = [(estado_inicial, encontrar_posicion_vacia(estado_inicial), [])]
    visitados = set()

    while pila:
        tablero, pos_vacia, camino = pila.pop()
        if tablero == estado_final:
            return camino  # Devuelve el camino (secuencia de movimientos)
        
        visitados.add(tuple(map(tuple, tablero)))  # Marcar como visitado
        
        for movimiento in obtener_movimientos(pos_vacia):
            nuevo_tablero = intercambiar(tablero, pos_vacia, movimiento)
            if tuple(map(tuple, nuevo_tablero)) not in visitados:
                pila.append((nuevo_tablero, movimiento, camino + [nuevo_tablero]))
    
    return None  # No hay solución

# Función para encontrar la posición vacía en el tablero
def encontrar_posicion_vacia(tablero):
    for fila in range(2):
        for col in range(2):
            if tablero[fila][col] ==  0:  # Suponiendo que el 0 representa la casilla vacía
                return fila, col

def validar_un_caracter(entrada):
    return len(entrada) <= 1

def leer_entrys():
    btnJugar.config(state="disabled")
    btnLimpiar.config(state="normal")
    text1 = int(lblFicha1.get())
    text2 = int(lblFicha2.get())
    text3 = int(lblFicha3.get())
    text4 = int(lblFicha4.get())
    # text1f = lblFicha1f.get()
    # text2f = lblFicha2f.get()
    # text3f = lblFicha3f.get()
    # text4f = lblFicha4f.get()
    lblFicha1.config(state="disabled")
    lblFicha2.config(state="disabled")
    lblFicha3.config(state="disabled")
    lblFicha4.config(state="disabled")
    estado_inicial = [[text1, text2], [text3, text4]]  # El 0 representa la casilla vacía
    estado_final = [[0, 3], [1, 2]]
    # Ejecutar búsqueda en amplitud
    resultado_amplitud = busqueda_amplitud(estado_inicial, estado_final)
    text_box.insert(tk.END, "Búsqueda en Amplitud:\n")
    for paso in resultado_amplitud:
        text_box.insert(tk.END, f"{paso}\n")  # Agregar cada paso al text_box1

     # Ejecutar búsqueda en profundidad
    resultado_profundidad = busqueda_profundidad(estado_inicial, estado_final)
    text_box1.insert(tk.END, "Búsqueda en Profundidad:\n")
    for paso1 in resultado_profundidad:
        text_box1.insert(tk.END, f"{paso1}\n")  # Agregar cada paso al text_box1



def Limpiar_Contenido():
    lblFicha1.config(state="normal")
    lblFicha2.config(state="normal")
    lblFicha3.config(state="normal")
    lblFicha4.config(state="normal")
    lblFicha1.delete(0, tk.END)
    lblFicha2.delete(0, tk.END)
    lblFicha3.delete(0, tk.END)
    lblFicha4.delete(0, tk.END)
    # lblFicha1f.delete(0, tk.END)
    # lblFicha2f.delete(0, tk.END)
    # lblFicha3f.delete(0, tk.END)
    # lblFicha4f.delete(0, tk.END)
    text_box.delete(1.0, tk.END)
    text_box1.delete(1.0, tk.END)
    btnJugar.config(state="normal")
    btnLimpiar.config(state="disabled")
    


# Ventana principal
root = tk.Tk()
root.title("Práctica 2: Juego de las Fichas")
root.geometry("800x600+400+100")
root.resizable(False, False)
root.config(bg="lightblue") 

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
lblFicha1f.insert(0,'0')
lblFicha1f.config(justify="center")
lblFicha2f = tk.Entry(root, width=2, font=("Aptos", 40))
lblFicha2f.place(x= 90, y=395)
lblFicha2f.insert(0,'3')
lblFicha2f.config(justify="center")
lblFicha3f = tk.Entry(root, width=2, font=("Aptos", 40))
lblFicha3f.place(x= 30, y=460)
lblFicha3f.insert(0,'1')
lblFicha3f.config(justify="center")
lblFicha4f = tk.Entry(root, width=2, font=("Aptos", 40))
lblFicha4f.place(x= 90, y=460)
lblFicha4f.insert(0,'2')
lblFicha4f.config(justify="center")
text_box = tk.Text(root, width=20, height=10, font=("Helvetica", 16))  # Fuente más grande
text_box.place(x=200, y=120)


text_box1 = tk.Text(root, width=22, height=10, font=("Helvetica", 16))  # Fuente más grande
text_box1.place(x=500, y=120)


lblcola = tk.Label(root, text="Cola", font=("Aptos", 20))
lblcola.place(x=300 , y=75)
lblcola.config(bg="lightblue")

lblpila = tk.Label(root, text="Pila", font=("Aptos", 20))
lblpila.place(x=600 , y=75)
lblpila.config(bg="lightblue")




root.mainloop() 

