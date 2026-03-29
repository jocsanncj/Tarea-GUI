import tkinter as tk
import pygame as pg
from PIL import Image, ImageTk, ImageDraw


#Función para redondear las imágenes de la ficha personal
def imagen_redondeada(ruta, ancho, alto, radio):
    img = Image.open(ruta).resize((ancho, alto), Image.LANCZOS) #LANCZOS es un filtro de alta calidad para redimensionar imágenes, lo que ayuda a mantener la calidad de la imagen
    
    marco = Image.new('L', (ancho, alto), 0)
    draw = ImageDraw.Draw(marco)
    draw.rounded_rectangle((0, 0, ancho, alto), radius=radio, fill=255)
    
    resultado = Image.new('RGBA', (ancho, alto), (0, 0, 0, 0))
    resultado.paste(img, mask=marco)


def reproducir(): #Función para reproducir la música de fondo
    pg.mixer.music.play()
    pg.mixer.music.unpause()


def pausar(): #Función para pausar la música de fondo
    pg.mixer.music.pause()


def reiniciar(): #Función para reiniciar la música de fondo
    pg.mixer.music.stop()
    pg.mixer.music.play()


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


    ventfip.mainloop() 