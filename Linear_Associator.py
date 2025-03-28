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

    marco_x = ttk.LabelFrame(tabla_frame, text="Vectores Y", padding=(10,10), style="My.TFrame")
    marco_x.grid(row=0, column=0, padx=10, pady=10)

    global valores_y
    valores_y = [[] for _ in range(p)] 

    for i in range(p):
        ttk.Label(marco_x, text=f"y^{i+1}:", font=(font_size, size_letter), background="lightblue").grid(row=0, column=i+1, padx=5, pady=5)
        for j in range(n):
            entrada = ttk.Entry(marco_x, width=2, font=(font_size, size_letter))
            entrada.grid(row=j+1, column=i+1, padx=5, pady=5)
            valores_y[i].append(entrada)

    marco_y = ttk.LabelFrame(tabla_frame, text="Vectores X", padding=(10,10), style="My.TFrame")
    marco_y.grid(row=0, column=1, padx=10, pady=10)

    global valores_x
    valores_x = [[] for _ in range(p)]  

    for i in range(p):
        ttk.Label(marco_y, text=f"x^{i+1}:", font=(font_size, size_letter), background="lightblue").grid(row=0, column=i+1, padx=5, pady=5)
        for j in range(p):
            entrada = ttk.Entry(marco_y, width=2, font=(font_size, size_letter))
            entrada.grid(row=j+1, column=i+1, padx=5, pady=5)
            valores_x[i].append(entrada)
    
            if j == i: 
                entrada.insert(0, 1) 
            else:  
                entrada.insert(0, 0)  
            entrada.config(state="readonly")  
    

def custom_multiply(y, x):
    result = []
    for yi in y:
        if yi == x:
            result.append(1)
        else:
            result.append(0)
    return np.array(result)

def obtener_valores():
    valores_y_final = []
    for col in valores_y:
        col_valores = []
        for entry in col:
            try:
                col_valores.append(int(entry.get())) 
            except ValueError:
                col_valores.append(0)  
        valores_y_final.append(col_valores)
    
    valores_x_final = []
    for col in valores_x:
        col_valores = []
        for entry in col:
            try:
                col_valores.append(int(entry.get())) 
            except ValueError:
                col_valores.append(0)  
        valores_x_final.append(col_valores)
   


    matrices_Y = [np.array(val) for val in valores_y_final]
    matrices_X = [np.array(val) for val in valores_x_final]
   
    x =len(valores_x_final)
    y = len(valores_y_final[0])
    matriz_resultante = np.zeros((x, y), dtype=int)

    resultados_texto = ""

    for i in range(x):
        resultado = custom_multiply(matrices_Y[i], 1) 
        matriz_resultante[i] = resultado

    matriz = np.dot(matrices_X,matriz_resultante)
    
    resultados_texto += "- Linear Asssociator -\n"
   
    matriz_transpuesta = np.transpose(matriz_resultante)
    for fila in matriz_transpuesta:
        resultados_texto += ' '.join(map(str, fila)) + '\n'


    resultados_texto += "\n- Patrones Recuperados -\n"

    titulos = ""
    for i in range(1, len(matriz) + 1):
        titulos += f'Patrón {i}:'.ljust(15)  
    resultados_texto += titulos + '\n'

    longitud_patrones = len(matriz[0])

    for fila_index in range(longitud_patrones): 
        fila_texto = ""
        for fila in matriz: 
            fila_texto += str(fila[fila_index]).ljust(25) 
        resultados_texto += fila_texto + '\n' 

    resultado_final_label.config(text=resultados_texto)



# Ventana principal
root = tk.Tk()
root.title("Práctica 4: Linear Associator")
root.geometry("900x650+400+100")
root.resizable(False, False)
root.config(bg="lightblue") 

style = ttk.Style()
style.configure("My.TFrame", background="lightblue")

lblPatron = ttk.Label(root, text="No. de patrones: ", background="lightblue", font=(font_size, size_letter)).place(x=0, y=40)
txtPatron = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtPatron.place(x=120, y=40)

lblDimension = ttk.Label(root, text="Dimensión de m:", background="lightblue", font=(font_size, size_letter)).place(x=0, y=70)
txtDimension = ttk.Entry(root, width=3, font=(font_size, size_letter))
txtDimension.place(x=120, y=70)

mostrar_button = ttk.Button(root, text="Crea Vectores", command=mostrar_tabla)
mostrar_button.place(x=200, y=20)

guardar_button = ttk.Button(root, text="Linear Associator", command=obtener_valores)
guardar_button.place(x=200, y=60)

tabla_frame = ttk.Frame(root, style="My.TFrame")
tabla_frame.place(x=300, y=10)

resultado_final_label = ttk.Label(root, text="", font=(font_size, size_letter))
resultado_final_label.place(x=0, y=200)  

root.mainloop()
