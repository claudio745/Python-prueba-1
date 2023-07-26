##Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro
##usando la primera función. (10 puntos)


def calculo_area(radio):
    pi = 3.14
    area = (radio * radio) * pi
    return(area)
    
def calculo_cilindro(radio, altura):
    pi = 3.14
    volumen = pi * (radio * radio) * altura
    return(volumen)

def main():
    radio = float(input("Ingrese el radio: "))
    altura = float(input("Ingrese la altura: "))
    
    resultado = calculo_area(radio)
    resultado2 = calculo_cilindro(radio, altura)
    
    print("El area del circulo es: ", resultado)
    print("El volumen del cilindro es:", resultado2)

   
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    