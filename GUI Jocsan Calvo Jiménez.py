import tkinter as tk
import pygame as pg
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


#Función asociada a 'Análisis de números'
def pares(num):
    if isinstance (num, int) and num > 0:
        return pares_aux(num, 1)
                                    #Realmente esta parte de la función no sirve porque la ventana emergente es la que da los errores, pero si se ejecuta sola, sirve
    else:
        return 'Digite un  símbolo válido'

def pares_aux(num, op):
    if op > int(num ** 0.5): #Permite extender la cantidad de números a revisar, ya que tendría un límite de 1000
        return ""
    
    if num % op == 0:
        return f"({op}, {num//op}) " + pares_aux(num, op + 1)

    else:
        return pares_aux(num, op + 1)
    

#Función para redondear las imágenes de la ficha personal
def imagen_redondeada(ruta, ancho, alto, radio):
    img = Image.open(ruta).resize((ancho, alto), Image.LANCZOS) #LANCZOS es un filtro de alta calidad para redimensionar imágenes, lo que ayuda a mantener la calidad de la imagen
    
    marco = Image.new('L', (ancho, alto), 0)
    draw = ImageDraw.Draw(marco)
    draw.rounded_rectangle((0, 0, ancho, alto), radius=radio, fill=255)
    
    resultado = Image.new('RGBA', (ancho, alto), (0, 0, 0, 0))
    resultado.paste(img, mask=marco)
    
    return ImageTk.PhotoImage(resultado)

def reproducir(): #Función para reproducir la música de fondo
    pg.mixer.music.play()
    pg.mixer.music.unpause()

def pausar(): #Función para pausar la música de fondo
    pg.mixer.music.pause()

def reiniciar(): #Función para reiniciar la música de fondo
    pg.mixer.music.stop()
    pg.mixer.music.play()


#Función que ejecuta'Análisis de números'
def ex_an ():
    if ventprincipal.sec is not None: #Cambiar  a la ventana secundaria si ya existe una abierta, para evitar abrir varias ventanas de análisis de números u otras a la vez
        ventprincipal.sec.destroy()


    #Configuración de la ventana de análisis de números
    ventpares = tk.Toplevel()
    ventprincipal.sec = ventpares
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


    def calcular():
        numero = cnumero.get() #Obtiene el número escrito en el entry
        
        if numero == '':
         messagebox.showerror('Error', 'Digite un número') #Muestra un mensaje de error si el entry está vacío
         return
        
        if not numero.isdigit():
            messagebox.showerror('Error', 'Solo se permiten números enteros') #Muestra un mensaje de error si se escribe algo que no es un número
            return
        
        if int(numero) > 100000:
            messagebox.showerror('Error', 'El número es demasiado grande, por favor ingrese un número menor a 100000') #Muestra un mensaje de error si el número es demasiado grande
            return
        
        resultado1 = pares(int(numero))
        canvapares.itemconfig(textresult, text= 'Los múltiplos del número son: ' + resultado1) #Muestra el resultado en el canva

    cnumero = tk.Entry(ventpares, width= 35)
    cnumero.place(relx=0.5, rely=0.5, anchor='center')

    calc = tk.Button(ventpares, text= 'Calcular', width= 6, height= 1, command= lambda: calcular())
    calc.place(x= 250, y= 341)

    def limpiar(): #Función para limpiar el entry y los pares del canva
        cnumero.delete(0, 'end')
        canvapares.itemconfig(textresult, text='')

    def cerrar_an(): #Función para cerrar la ventana de análisis de números y volver al menú principal
        ventpares.destroy()
    
    limp = tk.Button(ventpares, text= 'Limpiar', width= 6, height= 1, command= lambda: limpiar())
    limp.place(x= 349, y= 341)

    botonmenu = tk.Button(ventpares, text= 'Menú principal', command= lambda: cerrar_an())
    botonmenu.place(x= 270, y= 600)
    
    canvapares.pack()



#Función que ejecuta 'Ficha personal'
def ex_fip ():
    if ventprincipal.sec is not None: #Cambiar  a la ventana secundaria si ya existe una abierta, para evitar abrir varias ventanas de ficha personal u otras a la vez
        ventprincipal.sec.destroy()

    #Configuración de la ventana de ficha personal
    ventfip = tk.Toplevel() #Se usa toplevel para crear una ventana secundaria, ya que si se usa Tk, se crearía una nueva ventana principal, lo que no es lo que se quiere
    ventprincipal.sec = ventfip
    ventfip.title('Ficha personal')
    ventfip.geometry('750x750')
    ventfip.resizable(width= False, height= False)

    #Configuración del canva de ficha personal
    canvafip = tk.Canvas(ventfip, bg= 'White')
    canvafip.config(width=742, height= 742)

    #Texto de la ficha personal en el canva
    canvafip.create_text(371, 40, text= 'Jocsan Calvo Jiménez', font = ('Segoe UI', 20))
    canvafip.create_text(371, 70, text= '2026004788', font = ('Segoe UI', 10))
    canvafip.create_text(465, 180, text= 'Mi cumpleaños es el 17 de marzo y tengo 18 años. Soy de Cartago, específicamente de Cot, Oreamuno, un lugar medianamente tranquilo hasta hace poco. Realmente es una casualidad que esté en el TEC pero la carrera me gusta hasta el momento. Me gusta dormir, comer y escuchar música (escucho de todo un poco). He jugado varios videojuegos en mi vida aunque realmente soy malo en todos', width= 500, justify= 'left', font = ('Segoe UI', 12))
    canvafip.create_text(390, 526, text= 'Artic Monkeys', font = ('Segoe UI', 20))
    canvafip.create_text(352, 560, text= 'Whyd You Only Call Me When Youre High', font = ('Segoe UI', 10))
    canvafip.create_text(395, 590, text= 'Género musical: Indie Rock', font = ('Segoe UI', 10))

    #Agrega la imagen del programador al canva
    yomero = imagen_redondeada('FotoYo.png', 167, 200, 15)
    canvafip.create_image(120, 210, image=yomero)
    canvafip.image1 = yomero

    #Agrega la imagen del lugar al canva
    lugar = imagen_redondeada('FotoCot.png', 260, 170, 15)
    canvafip.create_image(371, 371, image=lugar)
    canvafip.image2 = lugar

    #Agrega la imagen del artista al canva
    artista = imagen_redondeada('ArticMonkeys.png', 200, 200, 15)
    canvafip.create_image(600, 610, image= artista)
    canvafip.image3 = artista

    canvafip.pack()

    pg.mixer.init() #Inicia el mezclador de pygame
    pg.mixer.music.load('Whyd You Only Call Me When Youre High.mp3')

    #Configura los botones de reproducción, pausa y reinicio de la música
    marcofip = tk.Frame(canvafip)
    marcofip.columnconfigure(0, weight=1)
    marcofip.columnconfigure(1, weight=1)
    marcofip.columnconfigure(2, weight=1)

    botonrep = tk.Button(marcofip, text='Reproducir', command= lambda: reproducir())
    botonrep.grid(row=0, column=0)

    botonpau = tk.Button(marcofip, text='Pausar', command= lambda: pausar())
    botonpau.grid(row=0, column=1)

    botonrei = tk.Button(marcofip, text='Reiniciar', command= lambda: reiniciar())
    botonrei.grid(row=0, column=2)

    marcofip.place(x= 388, y= 630, anchor='center')

    def cerrar_fip(): #Función para cerrar la ventana de ficha personal y volver al menú principal
        ventfip.destroy()

    botonmenu = tk.Button(ventfip, text= 'Menú principal', command= lambda: cerrar_fip())
    botonmenu.place(x= 328, y= 715)

#Configuración de la ventana principal
ventprincipal = tk.Tk()
ventprincipal.title('Tarea')
ventprincipal.geometry('650x650')
ventprincipal.resizable(width = False, height = False)
ventprincipal.sec = None #Variable para almacenar la ventana secundaria

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
boton1 = tk.Button(marco1, text='Análisis de números', width= 19, height= 5, font= ('Segoe UI', 12), command= lambda: ex_an())
boton1.grid(row=0, column=0)

#Botón para ejecutar 'Ficha personal'
boton2 = tk.Button(marco1, text='Ficha personal', width= 19, height= 5, font= ('Segoe UI', 12), command= lambda: ex_fip())
boton2.grid(row=0, column=1)

#Botón para ejecutar 'Animación'
boton3 = tk.Button(marco1, text='Animación', width= 19, height= 5, font= ('Segoe UI', 12))
boton3.grid(row=0, column=2)

marco1.place(relx=0.5, rely=0.5, anchor='center')


ventprincipal.mainloop()