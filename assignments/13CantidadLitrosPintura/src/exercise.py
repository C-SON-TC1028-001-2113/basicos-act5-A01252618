import math
def main():
    #escribe tu código abajo de esta línea
    print("ingrese los valores para la coordenada 1")
    x1 = int(input("Cuál es el valor de x1?"))
    y1 = int(input("Cuál es el valor de y1?"))
    print("ingrese los valores para la coordenada 2")
    x2 = int(input("Cuál es el valor de x2?"))
    y2 = int(input("Cuál es el valor de y2?"))

    distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("la distancia entre la coordenada 1 y la coordenada 2 es =", distancia)

    area = lado1 * lado2
    litros = area / cantidad


    print ("El area a pintar en metros es: "+str(area))
    print ("El rendimiento es: "+str(area))
    print ("Se necesitan: "+str(litros))

if __name__ == '__main__':
    main()
