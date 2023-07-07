class Producto:
    """ Clase que implenta producto"""
    def __init__(self,codigo,nombre,precio,placa,color,motor) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.placa = placa
        self.color = color
        self.motor = motor
        pass
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|{}|{}|".format(self.codigo,
                                      self.nombre,
                                      self.precio,
                                      self.placa,
                                      self.color,
                                      self.motor,)