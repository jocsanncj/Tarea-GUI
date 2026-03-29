import tkinter as tk
import pygame as pg


#Función que ejecuta 'Ficha personal'
def ex_fip ():
    #Configuración de la ventana de ficha personal
    ventfip = tk.Toplevel() #Se usa toplevel para crear una ventana secundaria, ya que si se usa Tk, se crearía una nueva ventana principal, lo que no es lo que se quiere
    ventfip.title('Ficha personal')
    ventfip.geometry('750x750')
    ventfip.resizable(width= False, height= False)

    #Configuración del canva de ficha personal
    canvafip = tk.Canvas(ventfip, bg= 'White')
    canvafip.config(width=742, height= 742)
    canvafip.create_text(371, 40, text= 'Jocsan Calvo Jiménez', font = ('Segoe UI', 20))
    canvafip.create_text(371, 70, text= '2026004788', font = ('Segoe UI', 10))
    canvafip.create_text(465, 180, text= 'Mi cumpleaños es el 17 de marzo y tengo 18 años. Soy de Cartago, específicamente de Cot, Oreamuno, un lugar medianamente tranquilo hasta hace poco. Realmente es una casualidad que esté en el TEC pero la carrera me gusta hasta el momento. Me gusta dormir, comer y escuchar música (escucho de todo un poco). He jugado varios videojuegos en mi vida aunque realmente soy malo en todos', width= 500, justify= 'left', font = ('Segoe UI', 12))
    canvafip.create_text(390, 526, text= 'Artic Monkeys', font = ('Segoe UI', 20))
    canvafip.create_text(352, 560, text= 'Whyd You Only Call Me When Youre High', font = ('Segoe UI', 10))
    canvafip.create_text(395, 590, text= 'Género musical: Indie Rock', font = ('Segoe UI', 10))

    ventfip.mainloop()