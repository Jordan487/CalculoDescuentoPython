def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento sobre un monto total de compra.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Tupla con el descuento calculado y el monto final a pagar.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final


# Llamadas a la función
monto1 = 100
descuento1, total1 = calcular_descuento(monto1)

monto2 = 200
descuento2, total2 = calcular_descuento(monto2, 15)

# Mostrar resultados
print(f"Monto total: {monto1}, Descuento: {descuento1}, Monto final: {total1}")
print(f"Monto total: {monto2}, Descuento: {descuento2}, Monto final: {total2}")