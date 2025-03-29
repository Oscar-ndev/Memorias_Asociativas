import tkinter as tk
from tkinter import ttk
import numpy as np  

size_letter = 12
font_size = "aptos"

valores_x = []

def mostrar_tabla():
    global n
    n = int(txtDimension.get())
    p = int(txtPatron.get())
    
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

    marco_y = ttk.LabelFrame(tabla_frame, text="Vectores X", padding=(10,10), style="My.TFrame")
    marco_y.grid(row=0, column=1, padx=10, pady=10)
    
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


    resultados_texto = " "    
    x =len(valores_x_final)
    matrices_X = [np.array(val).reshape(-1, 1) for val in valores_x_final] 
    matrices_productos = []
    suma_matrices = np.zeros((n, n), dtype=int) 

    for matriz in matrices_X:
        matriz_producto = matriz @ matriz.T
        np.fill_diagonal(matriz_producto, 0) 
        matrices_productos.append(matriz_producto)
        suma_matrices += matriz_producto  
    resultados_texto += "- Memoria Hopfield -\n"
    resultados_texto += f"{suma_matrices}\n\n\n"
    for i in range(x):
        resultado_multiplicacion = suma_matrices @ matrices_X[i]
        matriz_actual = matrices_X[i]
        resultado_evaluado = np.where(resultado_multiplicacion > 0, 1, np.where(resultado_multiplicacion < 0, -1, 0))
        while True:

            if not np.array_equal(resultado_evaluado, matriz_actual):
                matriz_actual = resultado_evaluado.copy() 
                resultado_multiplicacion = suma_matrices @ matriz_actual
                resultado_evaluado = np.where(resultado_multiplicacion > 0, 1, np.where(resultado_multiplicacion < 0, -1, 0))
            else: break
        resultados_texto += f"Patrón {i + 1} recuperado:\n{resultado_evaluado}\n\n"
    resultado_final_label.config(text=resultados_texto)

# Ventana principal
root = tk.Tk()
root.title("Memoria Hopfield")
root.geometry("900x650+400+100")
root.resizable(False, False)
root.config(bg="lightblue") 

style = ttk.Style()
style.configure("My.TFrame", background="lightblue")

lblPatron = ttk.Label(root, text="No. de patrones: ", background="lightblue", font=(font_size, size_letter)).place(x=0, y=40)
txtPatron = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtPatron.place(x=120, y=40)

lblDimension = ttk.Label(root, text="Dimensión de x:", background="lightblue", font=(font_size, size_letter)).place(x=0, y=70)
txtDimension = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtDimension.place(x=120, y=70)

mostrar_button = ttk.Button(root, text="Crea Vectores", command=mostrar_tabla)
mostrar_button.place(x=200, y=20)

guardar_button = ttk.Button(root, text="Hopfield", command=obtener_valores)
guardar_button.place(x=200, y=60)

tabla_frame = ttk.Frame(root, style="My.TFrame")
tabla_frame.place(x=300, y=10)

resultado_final_label = ttk.Label(root, text="", font=(font_size, size_letter))
resultado_final_label.place(x=0, y=100)  

root.mainloop()
