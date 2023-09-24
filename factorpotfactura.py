
from math import*


p_activa = 10750
p_reactiva = 8250
angulodeseado = acos(0.91)
volt = 380
nfases = 3
freq = 50





def main():

    anguloinicial = atan(tan((8250 / 10750)))

    print('Este es el angulo inicial: ' + str(anguloinicial))

    p_aparente_inicial = (p_activa / cos(anguloinicial))

    print ('Esta es la potencia  aparente inicial: ' + str(p_aparente_inicial) + ' Kw')

    qc = (p_activa * (tan(anguloinicial) - tan(angulodeseado)))

    print ('Esta es la potencia reactiva capacitiva: ' + str(qc) + ' Kwr')

    c = (qc * 1000000) / ((volt **2) * (2 * pi) * freq * nfases)

    print('Este es el banco de capacitores necesario: ' + str(c) + ' uF')

    qx = p_reactiva - qc

    print(str(qx) + 'Valor de QX')

    p_aparente_final = (p_activa / cos(angulodeseado))

    print('Esta es la potencia aparente final: ' + str(p_aparente_final) + ' Kw')

    p_reactiva_final = (p_aparente_final * sin(angulodeseado))

    print('Esta es la potencia reactiva final: ' + str(p_reactiva_final) + ' Kwr')
    













if __name__ == '__main__':
    main()