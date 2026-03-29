import tkinter as tk


#Función 'Animación'
def ex_bo():
    #Configuración de la ventana de animación
    ventbo = tk.Toplevel()
    ventbo.title('Animación')
    ventbo.geometry('650x690')
    ventbo.resizable(width=False, height=False)

    W, H = 642, 642 #Dimensiones del canva de animación


    #Configuración del canva de animación
    canvabo = tk.Canvas(ventbo, width=W, height=H, bg='black')
    canvabo.pack()


    ventbo.mainloop()