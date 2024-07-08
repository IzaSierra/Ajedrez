class Pieza:
  def __init__(self, color, nombre, fila, columna):
    self.color = color
    self.nombre = nombre
    self.fila = fila
    self.columna = columna
    
    def movimiento(self, nueva_posicion):
        pass
      
    def mover(self, nueva_posicion):
        if self.movimiento(nueva_posicion):
            self.posicion = nueva_posicion
            return f"La pieza ahora está en la posición: {nueva_posicion}"
        else:
            return "Movimiento Incorrecto, la pieza no se ha movido"
          
    