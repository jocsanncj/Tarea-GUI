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

    bolas = [ #Cada bola es una lista con la posición x, posición y, velocidad en x, velocidad en y, radio y color
        [100, 100, 4, 3, 30, 'green'],
        [400, 300, -3, 5, 30, 'blue'],
    ]

    velocidad = [1] #Define la velocidad de las bolas, para poder modificarla desde la función de animación

    circulos = [
        canvabo.create_oval(bolas[0][0]-bolas[0][4], bolas[0][1]-bolas[0][4], bolas[0][0]+bolas[0][4], bolas[0][1]+bolas[0][4], fill=bolas[0][5], outline=''),
        canvabo.create_oval(bolas[1][0]-bolas[1][4], bolas[1][1]-bolas[1][4], bolas[1][0]+bolas[1][4], bolas[1][1]+bolas[1][4], fill=bolas[1][5], outline='')
    ] #Crea listas para almacenar los hitboxes de las bolas para detectar colisiones


    def checar_choque():
        b1, b2 = bolas[0], bolas[1]
        dx = b2[0] - b1[0]  # Diferencia horizontal entre centros
        dy = b2[1] - b1[1]  # Diferencia vertical entre centros
        dist = (dx**2 + dy**2) ** 0.5  # Distancia entre centros (Pitágoras)

        if dist < b1[4] + b2[4] and dist > 0:  # Si la distancia es menor a la suma de radios, hay choque
            nx = dx / dist  
            ny = dy / dist  
            p = (b1[2]*nx + b1[3]*ny - b2[2]*nx - b2[3]*ny)  # Diferencia de velocidades en el eje de colisión
            b1[2] -= p * nx  
            b1[3] -= p * ny  
            b2[2] += p * nx  
            b2[3] += p * ny  
            overlap = (b1[4] + b2[4]) - dist
            b1[0] -= overlap/2 * nx  # Separa b1 del punto de choque
            b1[1] -= overlap/2 * ny
            b2[0] += overlap/2 * nx  # Separa b2 del punto de choque
            b2[1] += overlap/2 * ny

    def mover_bolas(i):
        if i >= len(bolas):  # Caso base: ya se movieron todas las bolas
            return
        b = bolas[i]
        b[0] += b[2] * velocidad[0]
        b[1] += b[3] * velocidad[0]  

        # Rebote con pared izquierda
        if b[0] - b[4] <= 0:
            b[0] = b[4]
            b[2] = abs(b[2])

        # Rebote con pared derecha
        if b[0] + b[4] >= W:
            b[0] = W - b[4]
            b[2] = -abs(b[2])

        # Rebote con pared superior
        if b[1] - b[4] <= 0:
            b[1] = b[4]
            b[3] = abs(b[3])
            
        # Rebote con pared inferior
        if b[1] + b[4] >= H:
            b[1] = H - b[4]
            b[3] = -abs(b[3])
        canvabo.coords(circulos[i], b[0]-b[4], b[1]-b[4], b[0]+b[4], b[1]+b[4])  # Actualiza posición en canvas
        mover_bolas(i + 1)  # Llamada recursiva con la siguiente bola

    def animar():
        mover_bolas(0)   # Mueve todas las bolas desde la primera
        checar_choque()  # Verifica y resuelve colisión entre las dos bolas
        ventbo.after(16, animar)  # Repite cada 16ms

    def aumentar():
        if velocidad[0] < 4:       # Límite máximo para no crashear
            velocidad[0] += 0.5

    def disminuir():
        if velocidad[0] > 0.5:     # Límite mínimo para no detener la animación
            velocidad[0] -= 0.5

    marco_bo = tk.Frame(ventbo)
    tk.Button(marco_bo, text='- Velocidad', command=disminuir).grid(row=0, column=0, padx=10)
    tk.Button(marco_bo, text='+ Velocidad', command=aumentar).grid(row=0, column=1, padx=10)
    marco_bo.pack(pady=5)

    animar()  # Inicia la animación



    ventbo.mainloop()