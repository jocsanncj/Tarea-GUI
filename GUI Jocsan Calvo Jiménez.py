import tkinter as tk

#Configuración de la ventana principal
ventprincipal = tk.Tk()
ventprincipal.title('Tarea')
ventprincipal.geometry('650x650')
ventprincipal.resizable(width = False, height = False)

#Configuración del canva principal
canva1 = tk.Canvas(ventprincipal, bg='#48C0D5')
canva1.config(width=642, height= 642)
canva1.create_text(321, 100, text= '¡Bienvenido!', font = ('Segoe UI', 28, 'bold'))
canva1.pack()


ventprincipal.mainloop()