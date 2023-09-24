# Importacion de modulos requeridos

from math import*




# Finalizado de Importacion de Modulos

# Establecimiento de Variables

sI = (100 * 750)
anguloinicial = acos(0.78)
angulodeseado = acos(0.92)
nfases = [1, 3] # Monofasico = 0  / Trifasico = 1
freq = 50
voltaje = [220, 380] # Monofasico = 0  / Trifasico = 1

vn = int(input('Para utilizar 220, pulsar 0, en caso contrario y sea 380 pulsar 1:      '))
fn = int(input('Para utilizar Monofasico, pulsar 0, en caso contrario y sea Trifasico pulsar 1:    '))

#Finalizacion de Establecimiento de Variables Globales

#Establecimiento de Variables Menu



#Finalizacion de Establecimiento de Variables Menu

#Establemiento de Funciones para el funcionamiento

def factorPotenciaGenerador():
    pass




def factorPotenciaMotor():

    print(str(sI) + ' W (Potencia Aparente Inicial)')
    print(str(degrees(anguloinicial)) + '° (Angulo Inicial)')

    potencia = sI * cos(anguloinicial)
    print(str(potencia) + ' W (Potencia Activa)')

    qci = potencia * (tan(anguloinicial))
    qcf = potencia * (tan(angulodeseado))

    qc = qci - qcf

    print(str(qc) + ' VAR (Potencia Reactiva Capacitiva)')

    cap_capacitor = (qc * 1000000) / ((voltaje[vn] ** 2) * ( 2 * pi) * freq * nfases[fn])

    print(str(cap_capacitor) + ' uF')

    ql = sI * sin(anguloinicial)

    qx = ql - qc

    print(str(ql) + '(Valor de QL)')

    print(str(qx) + '(Valor de QX)')

    sF = potencia / cos(angulodeseado)

    print(str(sF) + ' W (Potencia Aparente Final)')

    angulofinal = atan(qx / potencia)

    print(str(degrees(angulofinal)) + '° (Angulo Final)')

    mejoraRendimiento = ((sI - sF) / (sI)) * 100

    print(str(mejoraRendimiento) + '% (Mejora de Rendimiento)')
    

# Creacion de la Funcion Ejecutora

def main():

    factorPotenciaMotor()





if __name__ == '__main__':
    main()
