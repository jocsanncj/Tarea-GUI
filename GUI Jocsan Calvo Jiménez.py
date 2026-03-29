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

#Configuración del marco de los botones
marco1 = tk.Frame(ventprincipal)
marco1.columnconfigure(0, weight=1)
marco1.columnconfigure(1, weight=1)
marco1.columnconfigure(2, weight=1)

#Botón para ejecutar 'Análisis de números'
boton1 = tk.Button(marco1, text='Análisis de números', width= 19, height= 5, font= ('Segoe UI', 12))
boton1.grid(row=0, column=0)

#Botón para ejecutar 'Ficha personal'
boton2 = tk.Button(marco1, text='Ficha personal', width= 19, height= 5, font= ('Segoe UI', 12))
boton2.grid(row=0, column=1)

#Botón para ejecutar 'Animación'
boton3 = tk.Button(marco1, text='Animación', width= 19, height= 5, font= ('Segoe UI', 12))
boton3.grid(row=0, column=2)

marco1.place(relx=0.5, rely=0.5, anchor='center')


ventprincipal.mainloop()