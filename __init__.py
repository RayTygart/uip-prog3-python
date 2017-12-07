Palabra_secreta = "calixto"
acum = 1
#acum es un acomulador

print("\n\t\t\t\t\t\t\t JUEGO DIDACTICO DE LA PALABRA SECRETA")
print("\n Ingrese la palabra secreta, tienes 3 intentos. \n Por ser especial te dare la primera pista:")
print("\t Es el equivalente español de Romeo, de la novela ""Romeo & Julieta")

while acum < 4:

    print("\n Este es su intento #" + str(acum) + " de 3")
    # se hace uso del acumulador para que la persona sepa cuantos intentos lleva

    palabra = input("La palabra secreta es... = ")

    if palabra.lower() == "calixto":
        print("\n ¡Felicidades! Eres toda una eminencia literaria!!!")
        break
    else:
        print("\n RESPUESTA INCORRECTA.")
        acum = acum + 1
        if acum <4:
            print(" No pasa nada, aun tienes otro intento mas ")
    if acum == 2:
        print(" Vamos a darte otra ayudita: \n\t La novela donde sale este personaje, fue escrita por Fernando de Rojas y publicada en 1499.")
    if acum == 3:
        print(" HA - HAAA! Creiste que te daria otra pista, pero no. Intente nuevamente ")
    if acum == 4:
        print(" Gracias por participar! Vuelva Pronto!")