import tkinter as tk

#Función que ejecuta'Análisis de números'
def ex_an ():
    #Configuración de la ventana de análisis de números
    ventpares = tk.Toplevel()
    ventpares.title('Análisis de números')
    ventpares.geometry('650x650')
    ventpares.resizable (height= False, width= False)

    #Configuración del canva de análisis de números
    canvapares = tk.Canvas(ventpares, bg= '#A469D6')
    canvapares.config(width=642, height= 642)
    canvapares.create_text(321, 60, text= 'Análisis de números', font = ('Segoe UI', 28, 'bold'))
    canvapares.create_text(321, 110, text= 'Esta función le permitirá hallar los múltiplos de un número entero dado en pares, tal que (a * b) = n', font = ('Segoe UI', 10), width= 530, justify= 'center')
    canvapares.create_text(321, 301, text= 'Digite un número entero: ', font = ('Segoe UI', 10), width= 530, justify= 'left')
    textresult = canvapares.create_text(321, 450, text= '', font= ('Segoe UI', 18, 'bold'), width= 550, justify= 'center' )