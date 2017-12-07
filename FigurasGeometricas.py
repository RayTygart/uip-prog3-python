import time

class Figura(object):

    def Cono(self):
        while True:
            try:
                r = float(input("\n\t Introduzca el radio: "))
                a = float(input("\n\t Introduzca la altura: "))
                Volumen1 = ((r ** 2 * a) / 3) * 3.141592
                print("El volumen del cono es:", "{0:.2f}".format(Volumen1))
                break
            except ValueError:
                print(" NO VALIDO. INTENTE NUEVAMENTE ")
                time.sleep(1)

    def Cilindro(self):
        while True:
            try:
                r = float(input("\n\t Introduzca el radio: "))
                a = float(input("\n\t Introduzca la altura: "))
                Volumen2 = 3.141592 * r ** 2 * a
                print("El volumen del cilindro es:", "{0:.2f}".format(Volumen2))
                break
            except ValueError:
                print(" NO VALIDO. INTENTE NUEVAMENTE  ")
                time.sleep(1)

    def Esfera(self):
        while True:
            try:
                r = float(input("\n\t Introduzca el radio: "))
                Volumen3 = (4 / 3) * 3.141592 * r ** 3
                print("El volumen de la esfera es: ", "{0:.2f}".format(Volumen3))
                break
            except ValueError:
                print( " NO VALIDO. INTENTE NUEVAMENTE ")
                time.sleep(1)


class CEsfera(Figura):
    def formula(self):
        self.Esfera()


class CCilindro(Figura):
    def formula(self):
        self.Cilindro()


class CCono(Figura):
    def formula(self):
        self.Cono()