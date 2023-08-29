def validar_numero_en_base(numero, base):
    bases_validas = [2, 8, 10, 16]

    if base not in bases_validas:
        return False

    if base == 2:
        caracteres_validos = set("01")
    elif base == 8:
        caracteres_validos = set("01234567")
    elif base == 10:
        caracteres_validos = set("0123456789")
    elif base == 16:
        caracteres_validos = set("0123456789ABCDEF")

    numero = numero.upper() #para poner el numero en mayusculas
    for digito in numero:
        if digito not in caracteres_validos:
            return False

    return True          #comprueba en que base esta