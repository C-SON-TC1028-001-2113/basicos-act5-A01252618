import math
def main():
    #escribe tu código abajo de esta línea
    Area =float(input("Area a pintar en metros:"))
    Rendimiento =float(input("Rendimiento (m2/l): "))
    Litros =(int(math.ceil(Area/Rendimiento)))
    print("Litros a comprar: "+str(Litros))

    print ("El area a pintar en metros es: "+str(Area))
    print ("El rendimiento es: "+str(Rendimiento))
    print ("Se necesitan: "+str(Litros))

if __name__ == '__main__':
    main()
