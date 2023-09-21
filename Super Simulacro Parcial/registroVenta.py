# Creación del registro venta
class Venta:
    def __init__(self, num_venta, descri, monto, articulo, vendedor):
        self.numero = num_venta
        self.descripcion = descri
        self.monto = monto
        self.articulo = articulo
        self.vendedor = vendedor


# Función to string
def to_string_venta(registro):
    cadena = ''
    cadena += '{:<30}'.format('Número de venta: ' + str(registro.numero)) + ' || '
    cadena += '{:<40}'.format('Descripción: ' + registro.descripcion) + ' || '
    cadena += '{:<30}'.format('Monto de la venta: $' + str(registro.monto)) + ' || '
    cadena += '{:<30}'.format('Artículo: ' + str(registro.articulo)) + ' || '
    cadena += '{:<30}'.format('Vendedor: ' + str(registro.vendedor))

    return cadena
