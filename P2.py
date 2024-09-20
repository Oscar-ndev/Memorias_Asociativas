import tkinter as tk

def validar_un_caracter(entrada):
    return len(entrada) <= 1

def leer_entrys():
    txtFicha1 = lblFicha1.get()
    txtFicha2 = lblFicha2.get()
    txtFicha3 = lblFicha3.get()
    txtFicha4 = lblFicha4.get()
    btnJugar.config(bg="white", fg="black")
    lblFichas.config(text=f"Orden de fichas {txtFicha1}{txtFicha2}{txtFicha3}{txtFicha4}")


# Ventana principal
root = tk.Tk()
root.title("Práctica 2: Juego de las Fichas")
root.geometry("800x600+400+100")
root.resizable(False, False)

# Crear un botón
btnJugar = tk.Button(root, text="Jugar", command=leer_entrys, font=("Aptos", 20), bg="blue", fg="white")
btnJugar.pack()

btnLimpiar = tk.Button(root, text="Limpiar", font=("Aptos", 15), bg="green", fg="white")
btnLimpiar.place(x=690, y=1)

lblInitialState = tk.Label(root, text="Estado Inicial", font=("Aptos", 20))
lblInitialState.place(x=15 , y=15)

validacion = root.register(validar_un_caracter)
lblFicha1 = tk.Entry(root,validate="key", width=2, font=("Aptos", 20), validatecommand=(validacion, '%P'))
lblFicha1.place(x= 30, y=60)
lblFicha2 = tk.Entry(root,validate="key", width=2, font=("Aptos", 20), validatecommand=(validacion, '%P'))
lblFicha2.place(x= 65, y=60)
lblFicha3 = tk.Entry(root,validate="key", width=2, font=("Aptos", 20), validatecommand=(validacion, '%P'))
lblFicha3.place(x= 30, y=95)
lblFicha4 = tk.Entry(root,validate="key", width=2, font=("Aptos", 20), validatecommand=(validacion, '%P'))
lblFicha4.place(x= 65, y=95)

lblFinalState = tk.Label(root, text="Estado Final", font=("Aptos", 20))
lblFinalState.place(x=15 , y=350)

lblFicha1f = tk.Entry(root, width=2, font=("Aptos", 20))
lblFicha1f.place(x= 30, y=395)
lblFicha1f.config(state="readonly")
lblFicha2f = tk.Entry(root, width=2, font=("Aptos", 20))
lblFicha2f.place(x= 65, y=395)
lblFicha2f.config(state="readonly")
lblFicha3f = tk.Entry(root, width=2, font=("Aptos", 20))
lblFicha3f.place(x= 30, y=430)
lblFicha3f.config(state="readonly")
lblFicha4f = tk.Entry(root, width=2, font=("Aptos", 20))
lblFicha4f.place(x= 65, y=430)
lblFicha4f.config(state="readonly")


lblFichas = tk.Label(root, text="")
lblFichas.pack()





root.mainloop()



