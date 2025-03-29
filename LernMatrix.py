import tkinter as tk
from tkinter import ttk
import numpy as np  

size_letter = 12
font_size = "aptos"

valores_x = []
valores_y = []

def mostrar_tabla():
    n = int(txtDimension.get())
    p = int(txtPatron.get())
    
    for widget in tabla_frame.winfo_children():
        widget.destroy()

    marco_x = ttk.LabelFrame(tabla_frame, text="Vectores X", padding=(10,10), style="My.TFrame")
    marco_x.grid(row=0, column=0, padx=10, pady=10)

    global valores_x
    valores_x = [[] for _ in range(p)] 

    for i in range(p):
        ttk.Label(marco_x, text=f"x^{i+1}:", font=(font_size, size_letter), background="lightblue").grid(row=0, column=i+1, padx=5, pady=5)
        for j in range(n):
            entrada = ttk.Entry(marco_x, width=2, font=(font_size, size_letter))
            entrada.grid(row=j+1, column=i+1, padx=5, pady=5)
            valores_x[i].append(entrada)

    marco_y = ttk.LabelFrame(tabla_frame, text="Vectores Y", padding=(10,10), style="My.TFrame")
    marco_y.grid(row=0, column=1, padx=10, pady=10)

    global valores_y
    valores_y = [[] for _ in range(p)]  

    for i in range(p):
        ttk.Label(marco_y, text=f"y^{i+1}:", font=(font_size, size_letter), background="lightblue").grid(row=0, column=i+1, padx=5, pady=5)
        for j in range(p):
            entrada = ttk.Entry(marco_y, width=2, font=(font_size, size_letter))
            entrada.grid(row=j+1, column=i+1, padx=5, pady=5)
            valores_y[i].append(entrada)

            if j == i: 
                entrada.insert(0, 1) 
            else:  
                entrada.insert(0, 0)  
            entrada.config(state="readonly")  

def custom_multiply(x, y):
    result = []
    for xi in x:
        if xi == 1 and y == 1:
            result.append(1)
        else:
            result.append(-1)
    return np.array(result)

def obtener_valores():
    valores_x_final = []
    for col in valores_x:
        col_valores = []
        for entry in col:
            try:
                col_valores.append(int(entry.get())) 
            except ValueError:
                col_valores.append(0)  
        valores_x_final.append(col_valores)

    resultado_text = "\n".join([str(valores) for valores in valores_x_final])
    resultado_label.config(text=resultado_text)

    matrices_X = [np.array(val) for val in valores_x_final]

    matriz_resultante = np.zeros((3, 5), dtype=int)

    resultados_texto = ""

    resultado_1 = custom_multiply(matrices_X[0], 1) 
    matriz_resultante[0] = resultado_1
    resultados_texto += "Patron 1:\n"
    resultados_texto += str(matriz_resultante) + "\n\n"

    resultado_2 = custom_multiply(matrices_X[1], 1)  
    matriz_resultante[1] = resultado_2
    resultados_texto += "Patron 2:\n"
    resultados_texto += str(matriz_resultante) + "\n\n"

    resultado_3 = custom_multiply(matrices_X[2], 1)  
    matriz_resultante[2] = resultado_3
    resultados_texto += "Patron 3:\n"
    resultados_texto += str(matriz_resultante) + "\n\n"

    resultado_final_1 = np.dot(matriz_resultante, matrices_X[0]) if len(matrices_X) > 0 else []
    resultado_final_2 = np.dot(matriz_resultante, matrices_X[1]) if len(matrices_X) > 1 else []
    resultado_final_3 = np.dot(matriz_resultante, matrices_X[2]) if len(matrices_X) > 2 else []

    resultados_texto += "- Fase de Recuperación -\n"
    resultados_texto += f"{resultado_final_1}\n"
    resultados_texto += f"{resultado_final_2}\n"
    resultados_texto += f"{resultado_final_3}\n\n"

    resultados_fase_recuperacion = [resultado_final_1, resultado_final_2, resultado_final_3]
    nombres_y = ["y1", "y2", "y3"]

    matriz_V = []

    for i, resultado in enumerate(resultados_fase_recuperacion):
        valor_max = np.max(resultado)  
        matriz_v = [1 if val == valor_max else 0 for val in resultado]  
        matriz_V.append(matriz_v) 

    matriz_V = np.array(matriz_V)
    resultados_texto += "- Patrones Recuperados -\n"
    resultados_texto += f"{matriz_V}\n"
    resultado_final_label.config(text=resultados_texto)

# Ventana principal
root = tk.Tk()
root.title("Lernmatrix")
root.geometry("900x650+400+100")
root.resizable(False, False)
root.config(bg="lightblue") 

style = ttk.Style()
style.configure("My.TFrame", background="lightblue")

lblPatron = ttk.Label(root, text="No. de patrones: ", background="lightblue", font=(font_size, size_letter)).place(x=0, y=40)
txtPatron = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtPatron.place(x=120, y=40)

lblDimension = ttk.Label(root, text="Dimensión de X:", background="lightblue", font=(font_size, size_letter)).place(x=0, y=70)
txtDimension = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtDimension.place(x=120, y=70)

mostrar_button = ttk.Button(root, text="Crea Vectores", command=mostrar_tabla)
mostrar_button.place(x=200, y=20)

guardar_button = ttk.Button(root, text="Lernmatrix", command=obtener_valores)
guardar_button.place(x=200, y=60)

tabla_frame = ttk.Frame(root, style="My.TFrame")
tabla_frame.place(x=300, y=10)

label_bajo_y = ttk.Label(root, text="Matriz leída:", font=(font_size, size_letter))
label_bajo_y.place(x=0, y=100)

resultado_label = ttk.Label(root, text="", font=(font_size, size_letter))
resultado_label.place(x=0, y=130)  

resultado_final_label = ttk.Label(root, text="", font=(font_size, size_letter))
resultado_final_label.place(x=0, y=200)  

root.mainloop()
