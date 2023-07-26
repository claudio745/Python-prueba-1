##En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación
##comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
##pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla 
##con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada 
##por la puntuación del nivel. Vea la imagen adjunta.(10 puntos)




def puntaje(puntos):
    dinero = 2400
    resultado = 0
    if(puntos == 0.0):
        resultado = resultado + (float(dinero) * float(puntos))
    elif(puntos == 0.4):
        resultado = resultado + (float(dinero) * float(puntos))
    elif (puntos >= 0.6):
        resultado = resultado + (float(dinero) * float(puntos))
    return(resultado)
          
    
    
def main():
    puntos = float(input("Ingrese la puntuacion obtenida: "))
    result = puntaje(puntos)
    print(result)
        

if __name__ == '__main__':
    main()