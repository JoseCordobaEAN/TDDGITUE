def contar_vocales(cadena):
    """
    (str) -> int

    Cuenta las vocales en una cadena

    >>> contar_vocales('hola')
    2
    >>> contar_vocales('')
    0

    :param cadena: la cadena a evaluar
    :return: int el numero de vocales en la cadena
    """
    contador = 0
    for letrea in cadena:
        if letrea in 'aeiouAEIOU':
            contador += 1
    return contador