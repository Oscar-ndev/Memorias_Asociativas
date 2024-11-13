import tkinter as tk
from tkinter import ttk
import numpy as np

size_letter = 9
font_size = "aptos"

valores_x = []

def mostrar_tabla():
    global n, y
    n = int(txtDimensionx.get())
    p = int(txtPatron.get())
    y = int(txtDimensiony.get())
    
    for widget in tabla_frame.winfo_children():
        widget.destroy()

    marco_x = ttk.LabelFrame(tabla_frame, text="Patrones X", padding=(10,10), style="My.TFrame")
    marco_x.grid(row=0, column=0, padx=10, pady=10)

    global valores_x
    valores_x = [[] for _ in range(p)]

    for i in range(p):
        ttk.Label(marco_x, text=f"x^{i+1}:", font=(font_size, size_letter), background="lightblue").grid(row=0, column=i+1, padx=5, pady=5)
        for j in range(n):
            entrada = ttk.Entry(marco_x, width=2, font=(font_size, size_letter))
            entrada.grid(row=j+1, column=i+1, padx=5, pady=5)
            valores_x[i].append(entrada)

    marco_y = ttk.LabelFrame(tabla_frame, text="Patrones Y", padding=(10,10), style="My.TFrame")
    marco_y.grid(row=0, column=1, padx=10, pady=10)

    global valores_y
    valores_y = [[] for _ in range(p)]

    for i in range(p):
        ttk.Label(marco_y, text=f"y^{i+1}:", font=(font_size, size_letter), background="lightblue").grid(row=0, column=i+1, padx=5, pady=5)
        for j in range(y):
            entrada = ttk.Entry(marco_y, width=2, font=(font_size, size_letter))
            entrada.grid(row=j+1, column=i+1, padx=5, pady=5)
            valores_y[i].append(entrada)

def obtener_valores():
    valores_x_final = []
    for col in valores_x:
        colx_valores = []
        for entry in col:
            try:
                colx_valores.append(int(entry.get()))
            except ValueError:
                colx_valores.append(0)
        valores_x_final.append(colx_valores)

    valores_y_final = []
    for col in valores_y:
        coly_valores = []
        for entry in col:
            try:
                coly_valores.append(int(entry.get()))
            except ValueError:
                coly_valores.append(0)
        valores_y_final.append(coly_valores)

    matrices = calcular_matrices_aprendizaje(valores_x_final, valores_y_final)
    max_matrix = calcular_matriz_maxima(matrices)
    min_matrix = calcular_matriz_minima(matrices)

    comparar_vectores(max_matrix, min_matrix, valores_x_final)

def calcular_matrices_aprendizaje(valores_x_final, valores_y_final):
    lon = len(valores_x_final)
    lenx = len(valores_x_final[0])
    leny = len(valores_y_final[0])
    matrices = []
    for i in range(lon):
        aprendizaje = [[0] * lenx for _ in range(leny)]
        for x in range(lenx):
            for y in range(leny):
                if valores_y_final[i][y] == valores_x_final[i][x]:
                    aprendizaje[y][x] = 1
                elif valores_y_final[i][y] == 0 and valores_x_final[i][x] == 1:
                    aprendizaje[y][x] = 0
                elif valores_y_final[i][y] == 1 and valores_x_final[i][x] == 0:
                    aprendizaje[y][x] = 2
        matrices.append(aprendizaje)
    return matrices

def calcular_matriz_maxima(matrices):
    max_result = []
    for row in zip(*matrices):
        max_row = [max(cell) for cell in zip(*row)]
        max_result.append(max_row)
    return max_result

def calcular_matriz_minima(matrices):
    min_result = []
    for row in zip(*matrices):
        min_row = [min(cell) for cell in zip(*row)]
        min_result.append(min_row)
    return min_result

def obtener_resultado(valor_matriz, valor_vector):
    if valor_matriz == 0 and valor_vector == 0:
        return 0
    elif valor_matriz == 0 and valor_vector == 1:
        return 0
    elif valor_matriz == 1 and valor_vector == 0:
        return 0
    elif valor_matriz == 1 and valor_vector == 1:
        return 1
    elif valor_matriz == 2 and valor_vector == 0:
        return 1
    elif valor_matriz == 2 and valor_vector == 1:
        return 1

def comparar_matriz_con_vector(matriz, vector):
    resultado = []
    for fila in matriz:
        fila_resultado = [obtener_resultado(valor_matriz, valor_vector) for valor_matriz, valor_vector in zip(fila, vector)]
        resultado.append(fila_resultado)
    return np.array(resultado)

def comparar_vectores(max_matrix, min_matrix, valores_x_final):
    resultados_texto = ""
    resultados_texto += "Memoria Máx\n"
    for row in max_matrix:
        resultados_texto += f"{row}\n"
    resultados_texto += "\n\nMemoria Mín\n"
    for row in min_matrix:
        resultados_texto += f"{row}\n"

    for i, vector in enumerate(valores_x_final):
        resultado_max, vector_minimo_max = calcular_resultados(max_matrix, vector, 'max')
        resultado_min, vector_maximo_min = calcular_resultados(min_matrix, vector, 'min')

        resultados_texto += f"Resultados para x^{i+1}:\n"
        resultados_texto += "Vector columna con los mínimos de cada fila (max):\n"
        resultados_texto += f"{vector_minimo_max}\n"
        resultados_texto += "Vector columna con los máximos de cada fila (min):\n"
        resultados_texto += f"{vector_maximo_min}\n\n"

    resultado_final_label.config(text=resultados_texto)

def calcular_resultados(matriz, vector, tipo):
    resultado_matriz = comparar_matriz_con_vector(matriz, vector)
    if tipo == 'min':
        vector_columna = np.max(resultado_matriz, axis=1)
    else:
        vector_columna = np.min(resultado_matriz, axis=1)
    return resultado_matriz, vector_columna

# Ventana principal
root = tk.Tk()
root.title("Práctica 6: Memoria α-β")
root.geometry("900x650+400+100")
root.resizable(False, False)
root.config(bg="lightblue")

style = ttk.Style()
style.configure("My.TFrame", background="lightblue")

lblPatron = ttk.Label(root, text="No. de patrones: ", background="lightblue", font=(font_size, size_letter)).place(x=0, y=40)
txtPatron = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtPatron.place(x=120, y=40)

lblDimensionx = ttk.Label(root, text="Dimensión de x:", background="lightblue", font=(font_size, size_letter)).place(x=0, y=70)
txtDimensionx = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtDimensionx.place(x=120, y=70)

lblDimensiony = ttk.Label(root, text="Dimensión de y:", background="lightblue", font=(font_size, size_letter)).place(x=0, y=100)
txtDimensiony = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtDimensiony.place(x=120, y=100)

mostrar_button = ttk.Button(root, text="Crea Vectores", command=mostrar_tabla)
mostrar_button.place(x=200, y=20)

guardar_button = ttk.Button(root, text="α-β", command=obtener_valores)
guardar_button.place(x=200, y=60)

tabla_frame = ttk.Frame(root, style="My.TFrame")
tabla_frame.place(x=300, y=10)

resultado_final_label = ttk.Label(root, text="", font=(font_size, size_letter))
resultado_final_label.place(x=0, y=130)

root.mainloop()
