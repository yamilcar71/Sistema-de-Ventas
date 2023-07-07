from venta_detalle import VentaDetalle
class Venta:
    """Clse que implementa venta"""
    def __init__(self,numero, razon_social,detalle:VentaDetalle=[],total=0) -> None:
        self.serie = 'F005'
        self.numero = numero
        self.razon_social = razon_social
        self.detalle:list = detalle
        self.base_imponible=total/1.18
        self.igv=total-(total/1.18)
        self.total=total
        pass
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|{}|{}|{}|".format(self.serie,
                                            self.numero,
                                            self.razon_social,
                                            self.detalle,
                                            self.base_imponible,
                                            self.igv,
                                            self.total)