from pieza import *

class Peon(Pieza):
    def __init__(self, color, nombre,  fila, columna):
        super().__init__(color, nombre, fila, columna)


    def movimiento (self,fila, columna):
        if self.columna == columna:
            if self.fila == 2:
                if fila == self.fila + 1 or fila == self.fila + 2:
                    self.fila = fila
                    print(f"Peón movido a la posición ({fila}, {columna})")
            else:
                print("Movimiento inválido")
        else:  # Movimiento regular
            if fila == self.fila + 1:
                self.fila = fila
                print(f"Peón movido a la posición ({fila}, {columna})")
            else:
                print("Movimiento inválido")
                 

