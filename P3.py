import tkinter as tk
from tkinter import ttk
import numpy as np  # Importar numpy

size_letter = 12
font_size = "aptos"

# Lista para almacenar los valores de las celdas
valores_x = []
valores_y = []

# Función para mostrar la tabla
def mostrar_tabla():
    n = int(txtDimension.get())
    p = int(txtPatron.get())
    
    # Limpiar tabla previa
    for widget in tabla_frame.winfo_children():
        widget.destroy()

    # Añadir marco para el vector X
    marco_x = ttk.LabelFrame(tabla_frame, text="Vectores X", padding=(10,10), style="My.TFrame")
    marco_x.grid(row=0, column=0, padx=10, pady=10)

    # Inicializar la lista de valores para X
    global valores_x
    valores_x = [[] for _ in range(p)]  # Lista de listas para almacenar cada columna

    # Añadir celdas para X en forma vertical
    for i in range(p):
        ttk.Label(marco_x, text=f"x^{i+1}:", font=(font_size, size_letter), background="lightblue").grid(row=0, column=i+1, padx=5, pady=5)
        for j in range(n):
            entrada = ttk.Entry(marco_x, width=2, font=(font_size, size_letter))
            entrada.grid(row=j+1, column=i+1, padx=5, pady=5)
            # Guardar el Entry en la lista
            valores_x[i].append(entrada)

    # Añadir marco para el vector Y
    marco_y = ttk.LabelFrame(tabla_frame, text="Vectores Y", padding=(10,10), style="My.TFrame")
    marco_y.grid(row=0, column=1, padx=10, pady=10)

    # Inicializar la lista de valores para Y
    global valores_y
    valores_y = [[] for _ in range(p)]  # Cambié a p para que coincida con la cantidad de patrones

    # Añadir celdas para Y en forma vertical
    for i in range(p):
        ttk.Label(marco_y, text=f"y^{i+1}:", font=(font_size, size_letter), background="lightblue").grid(row=0, column=i+1, padx=5, pady=5)
        for j in range(p):
            entrada = ttk.Entry(marco_y, width=2, font=(font_size, size_letter))
            entrada.grid(row=j+1, column=i+1, padx=5, pady=5)
            # Guardar el Entry en la lista
            valores_y[i].append(entrada)

            if j == i: 
                entrada.insert(0, 1)  # 1 en la diagonal
            else:  
                entrada.insert(0, 0)  # 0 en las otras posiciones
            entrada.config(state="readonly")  # Hacer el campo de entrada solo lectura

# Función para aplicar la lógica de comparación
def custom_multiply(x, y):
    result = []
    for xi in x:
        # Aplicar la regla: si xi y y son ambos 1, el resultado es 1; sino, -1
        if xi == 1 and y == 1:
            result.append(1)
        else:
            result.append(-1)
    return np.array(result)

# Función para obtener los valores de la tabla
def obtener_valores():
    # Recoger los valores de X
    valores_x_final = []
    for col in valores_x:
        col_valores = []
        for entry in col:
            try:
                col_valores.append(int(entry.get()))  # Convertir el valor a entero
            except ValueError:
                col_valores.append(0)  # O manejar el error como prefieras
        valores_x_final.append(col_valores)

    # Actualizar el label con los valores
    resultado_text = "\n".join([str(valores) for valores in valores_x_final])
    resultado_label.config(text=resultado_text)

    # Convertir valores a matrices numpy
    matrices_X = [np.array(val) for val in valores_x_final]

    # Inicializar matriz resultante con ceros
    matriz_resultante = np.zeros((3, 5), dtype=int)

    # Inicializar el texto para los resultados
    resultados_texto = ""

    # Paso 1: Llenar la primera fila
    resultado_1 = custom_multiply(matrices_X[0], 1)  # Usar Y[0] como 1
    matriz_resultante[0] = resultado_1
    resultados_texto += "Patron 1:\n"
    resultados_texto += str(matriz_resultante) + "\n\n"

    # Paso 2: Llenar la segunda fila
    resultado_2 = custom_multiply(matrices_X[1], 1)  # Usar Y2 como 1
    matriz_resultante[1] = resultado_2
    resultados_texto += "Patron 2:\n"
    resultados_texto += str(matriz_resultante) + "\n\n"

    # Paso 3: Llenar la tercera fila
    resultado_3 = custom_multiply(matrices_X[2], 1)  # Usar Y3 como 1
    matriz_resultante[2] = resultado_3
    resultados_texto += "Patron 3:\n"
    resultados_texto += str(matriz_resultante) + "\n\n"

    # Multiplicaciones de la matriz resultante con X, X2 y X3
    resultado_final_1 = np.dot(matriz_resultante, matrices_X[0]) if len(matrices_X) > 0 else []
    resultado_final_2 = np.dot(matriz_resultante, matrices_X[1]) if len(matrices_X) > 1 else []
    resultado_final_3 = np.dot(matriz_resultante, matrices_X[2]) if len(matrices_X) > 2 else []

    # Mostrar resultados finales
    resultados_texto += "- Fase de Recuperación -\n"
    resultados_texto += f"{resultado_final_1}\n"
    resultados_texto += f"{resultado_final_2}\n"
    resultados_texto += f"{resultado_final_3}\n\n"

    # Actualizar el label con los resultados
    
    # Fase de recuperación: comparar el valor más alto de cada resultado final
    resultados_fase_recuperacion = [resultado_final_1, resultado_final_2, resultado_final_3]
    nombres_y = ["y1", "y2", "y3"]

# Crear matriz V
    matriz_V = []

    for i, resultado in enumerate(resultados_fase_recuperacion):
        valor_max = np.max(resultado)  # Valor máximo en el resultado actual
        matriz_v = [1 if val == valor_max else 0 for val in resultado]  # Crear matriz V con 1 donde esté el valor máximo
        matriz_V.append(matriz_v)  # Añadir a la lista de matrices V


    # Convertir matriz V en un array de NumPy y mostrarla
    matriz_V = np.array(matriz_V)
    #print("\nMatriz Y recuperadas:")
    #print(matriz_V)
    resultados_texto += "- Patrones Recuperados -\n"
    resultados_texto += f"{matriz_V}\n"
    resultado_final_label.config(text=resultados_texto)


# Ventana principal
root = tk.Tk()
root.title("Práctica 3: Lernmatrix")
root.geometry("900x650+400+100")
root.resizable(False, False)
root.config(bg="lightblue") 

style = ttk.Style()
style.configure("My.TFrame", background="lightblue")

# Entradas para n y p
lblPatron = ttk.Label(root, text="No. de patrones: ", background="lightblue", font=(font_size, size_letter)).place(x=0, y=40)
txtPatron = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtPatron.place(x=120, y=40)

lblDimension = ttk.Label(root, text="Dimensión de X:", background="lightblue", font=(font_size, size_letter)).place(x=0, y=70)
txtDimension = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtDimension.place(x=120, y=70)

# Botón para mostrar la tabla
mostrar_button = ttk.Button(root, text="Crea Vectores", command=mostrar_tabla)
mostrar_button.place(x=200, y=20)

# Botón para obtener los valores
guardar_button = ttk.Button(root, text="Lernmatrix", command=obtener_valores)
guardar_button.place(x=200, y=60)

# Marco para la tabla
tabla_frame = ttk.Frame(root, style="My.TFrame")
tabla_frame.place(x=300, y=10)

label_bajo_y = ttk.Label(root, text="Matriz leída:", font=(font_size, size_letter))
label_bajo_y.place(x=0, y=100)

# Añadir un label para mostrar los resultados
resultado_label = ttk.Label(root, text="", font=(font_size, size_letter))
resultado_label.place(x=0, y=130)  # Ajusta la posición según sea necesario

# Añadir un label para mostrar resultados finales
resultado_final_label = ttk.Label(root, text="", font=(font_size, size_letter))
resultado_final_label.place(x=0, y=200)  # Ajusta la posición según sea necesario

# Ejecutar la ventana
root.mainloop()
