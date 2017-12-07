import re
def evaluar(patron, palabras):
    """
    Evaluacion de Expresiones Regulares
    Este programa sencillo evalua una conjunto de palabras y determina si si cumplen con un patron especifico.
    Las palabras que deben cumplir son: "rap them", "tapeth", "apth ", "wrap/try", "sap tray", "87ap9th", "apothecary"
    Las palabras que no deben cumplir son: "aleht", "happy them", "tarpth", "Apt", "peth", "tarreth", "ddpdg"
    :param patron: el patron que sera utilizado para determinar si las palabras cumplen o no.
    :param palabras: cojunto de palabras que seran evaluadas contra el patron
    :return: palabras que cumplen y las que no cumplen.
    .. note:: El programa esta diseñado con un patron especificamente para las palabras que estan enlistadas
    .. warning:: Los patrones son sensible a mayusculas y minusculas
    Example::
        patron =[a-z]
        palabra1 = "carlos" -->cumple
        palabra2 = "Carlos" --> no cumple
    """
    return palabras


if __name__ == "__main__":
    patron = "[a|t|r|s|w|8][a|p|r|7][a|o|p|t]"
    palabras = ["rap them", "tapeth", "apth ", "wrap/try", "sap tray", "87ap9th", "apothecary", "aleht", "happy them", "tarpth", "Apt", "peth", "tarreth", "ddpdg"]


    for palabras in palabras:
        if re.match(patron, palabras):
            print("La palabra", palabras, "cumple con el patron.")
        else:
            print("La palabra", palabras, "no cumple el patron.")



