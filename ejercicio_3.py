#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y
#el año como pmuestra la imagen. (10 puntos)


def separar_dia(fecha):
    dia = fecha[0:2]
    return dia

def separar_mes(fecha):
    mes = fecha[3:5]
    return mes

def separar_agno(fecha):
    agno = fecha[6:]
    return agno
    
    
def main():
    fecha = input("Ingrese fecha de nacimiento: ")
    resultado_dia = separar_dia(fecha)
    resultado_mes = separar_mes(fecha)
    resultado_agno = separar_agno(fecha)
    
    print("Dia: ", resultado_dia)
    print("Mes: ", resultado_mes)
    print("Año: ", resultado_agno)
    
    
if __name__ == '__main__':
    main()