from FigurasGeometricas import Figura
import time
if __name__ == "__main__":

    while True:
        print(" \n\t\t\t\t\t\t\t\t\t\t CALCULADORA DE VOLUMEN")
        print(" \n\n\tFavor elegir uno de las siguientes figuras geometricas:")
        Opcion = int(input("\t\t 1. Esfera \n\t\t 2. Cilindro \n\t\t 3. Cono \n\t\t\t Su elección: "))


        if Opcion == 1:
            Figura().Esfera()
            break
        elif Opcion == 2:
            Figura().Cilindro()
            break
        elif Opcion == 3:
            Figura().Cono()
            break
        print("OPCIÓN EQUIVOCADA. INTENTE NUVEAMENTE")
        time.sleep(1)
