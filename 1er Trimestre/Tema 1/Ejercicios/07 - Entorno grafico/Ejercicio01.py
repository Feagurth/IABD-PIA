import tkinter as Tkinter
import tkinter.font as tkFont

tablero =  [[" " for count in range(3)] for count in range(3)]
#tablero = [["X", "X", "O"], ["O", "X", "O"], ["X", "X", "O"]]

frame_tablero = None
puntuacion = [0, 0]
jugador_humano = 0


def calcular_xy(a, b):
    print ([(a//b), (a%b)])
    return [(a//b), (a%b)]

def colocar_ficha(event):
    global jugador_humano
    global frame_tablero
    posicion = calcular_xy(int(event.widget._name), 3)
    ficha = "X" if jugador_humano else "O"
    tablero[posicion[0]][posicion[1]] = ficha

    repintar_botones(frame_tablero)


def pintar_tablero():
    global frame_tablero
    root = Tkinter.Tk()
    root.title("Tic Tac Toe")    
    root.geometry("200x225")
    root.resizable(0,0)    

    frame_informacion = Tkinter.Frame(root)
    frame_informacion.pack(side="top", pady=5)
    frame_informacion.config(width="150", height="25")
    
    var = Tkinter.StringVar()
    var.set(f"Ganadas: {puntuacion[0]} Perdidas: {puntuacion[1]}")

    label = Tkinter.Label(frame_informacion, textvariable=var, relief=Tkinter.FLAT )
    label.pack()

    if(frame_tablero == None):
        frame_tablero = Tkinter.Frame(root)        
        frame_tablero.pack(side="bottom", pady=20)

    pintar_botones(frame_tablero)

    root.mainloop()

def repintar_botones(contenedor):
    borrar_botones(contenedor)
    pintar_botones(contenedor)

def borrar_botones(contenedor):
    global frame_tablero
    master = contenedor.master
    contenedor.destroy()
    frame_tablero = Tkinter.Frame(master)
    frame_tablero.pack(side="bottom", pady=20)    

def pintar_botones(contenedor):
    global frame_tablero
    i = 0

    for x in tablero:
            # Iteramos por las oclumnas del tablero
            for y in range(0,3):
                texto = x[y]

                color = '#ff0000' if texto == "X" else "#00ff00"

                font = tkFont.Font(family="Helvetica", size=20, weight = tkFont.BOLD)

                f = Tkinter.Frame(contenedor, width=50, height=50)
                b = Tkinter.Button(f, name = str(i), text = texto, font = font, fg=color)
                b.bind('<Button-1>', colocar_ficha)

                f.rowconfigure(0, weight = 1)
                f.columnconfigure(0, weight = 1)
                f.grid_propagate(0)

                f.grid(row = int(i/3), column = int(i%3))
                b.grid(sticky = "NWSE")

                i += 1

def main():

    pintar_tablero()
        




if __name__ == "__main__":
    main()
