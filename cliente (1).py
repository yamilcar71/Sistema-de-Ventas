class Cliente:
    """ Clase que impleta cliente"""
    def __init__(self,dni,nombres,apellidos,direccion,telefono) -> None:
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        pass
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|{}|".format(self.dni,
                                      self.nombres,
                                      self.apellidos,
                                      self.direccion,
                                      self.telefono)