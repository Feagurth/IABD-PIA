import tkinter as Tkinter
import tkinter.font as tkFont

tablero =  [[" " for count in range(3)] for count in range(3)]
tablero = [["X", "X", "O"], ["O", "X", "O"], ["X", "X", "O"]]

puntuacion = [0, 0]
jugador_activo = 0


def calcular_xy(a, b):
    print (a // b)
    print(a%b)
    return [(a//b), (a%b)]

def colocar_ficha(event):
    print(event.widget._name)
    print(calcular_xy(int(event.widget._name), 3))


def pintar_tablero():
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

    frame_tablero = Tkinter.Frame(root)        
    frame_tablero.pack(side="bottom", pady=20)

    i = 0

    for x in tablero:
            # Iteramos por las oclumnas del tablero
            for y in range(0,3):
                
                texto = x[y];

                color = '#ff0000' if texto == "X" else "#00ff00"

                font = tkFont.Font(family="Helvetica", size=20, weight = tkFont.BOLD)

                f = Tkinter.Frame(frame_tablero, width=50, height=50)
                b = Tkinter.Button(f, name = str(i), text = texto, font = font, fg=color)
                b.bind('<Button-1>', colocar_ficha)

                f.rowconfigure(0, weight = 1)
                f.columnconfigure(0, weight = 1)
                f.grid_propagate(0)

                f.grid(row = int(i/3), column = int(i%3))
                b.grid(sticky = "NWSE")

                i += 1

    root.mainloop()

def main():

    pintar_tablero()
        




if __name__ == "__main__":
    main()
