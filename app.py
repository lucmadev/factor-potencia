import flet as ft
from math import*


nfases = 0
voltaje = 0
freq = 0





def main(page):
    def datacompartidos (e):

        def btnfreq50_clicked(e):
            global freq
            freq = 50

        def btnfreq60_clicked(e):
            global freq
            freq = 60

        def btnfase1_clicked(e):
            global nfases
            nfases = 1

        def btnfase3_clicked(e):
            global nfases
            nfases = 3

        def btnvoltaje220_clicked(e):
            global voltaje
            voltaje = 220

        def btnvoltaje380_clicked(e):
            global voltaje
            voltaje = 380
          
        btnfreq = ft.Row([
            ft.ElevatedButton(text="50Hz", on_click= btnfreq50_clicked),
            ft.ElevatedButton(text="60Hz", on_click=btnfreq60_clicked),
        ]
        )

        btnfase = ft.Row([
            ft.ElevatedButton(text="1 Fase", on_click= btnfase1_clicked),
            ft.ElevatedButton(text="3 Fases", on_click=btnfase3_clicked),
        ]
        )
        btnvoltaje = ft.Row([
            ft.ElevatedButton(text="220V", on_click=btnvoltaje220_clicked),
            ft.ElevatedButton(text="380V", on_click=btnvoltaje380_clicked),
        ]
        )
  
        page.add(ft.Column([
            btnfreq,
            btnfase,
            btnvoltaje,
            ])
        )
        



    def factorPotenciaMotor(e):
        potaparenteinicial = ft.TextField(label="Ingresa la potencia aparente: ", value=0)
        anguloinicial = ft.TextField(label="Ingresa el cosfi inicial: ", value=0.7)
        angulodeseado = ft.TextField(label="Ingresa el cosfi deseado: ", value=0.9)
        #frecuencia = ft.TextField(label="Ingresa la frecuencia: ")

        def calcular(e):
            potaparenteinicialvalue = int(potaparenteinicial.value)
            anguloinicialvalue = acos(float(anguloinicial.value))
            angulodeseadovalue = acos(float(angulodeseado.value))
            potencia = potaparenteinicialvalue * cos(anguloinicialvalue)
            qci = potencia * (tan(anguloinicialvalue))
            qcf = potencia * (tan(angulodeseadovalue))
            qc = qci - qcf
            cap_capacitor = (qc * 1000000) / ((voltaje ** 2) * ( 2 * pi) * freq * nfases)
            ql = potaparenteinicialvalue * sin(anguloinicialvalue)
            qx = ql - qc
            potaparentefinal = potencia / cos(angulodeseadovalue)
            angulofinal = degrees(atan(qx / potencia))
            mejoraRendimiento = ((potaparenteinicialvalue - potaparentefinal) / (potaparenteinicialvalue)) * 100
            
            page.add(ft.Column([
                ft.Text("La potencia activa es: " + str(potencia) + " W"),
                ft.Text("La potencia reactiva capacitiva es: " + str(qc) + " VAR"),
                ft.Text("La capacidad del capacitor es: " + str(cap_capacitor) + " uF"),
                ft.Text("Valor de QL: " + str(ql) + " VAR"),
                ft.Text("Valor de QX: " + str(qx) + " VAR"),
                ft.Text("La potencia aparente final es: " + str(potaparentefinal) + " W"),
                ft.Text("El angulo final es: " + str(angulofinal) + "°"),
                ft.Text("La mejora de rendimiento es de un: " + str(mejoraRendimiento) + "%"),
                ])
            )

        page.clean()

        page.add(ft.Column([
            potaparenteinicial,
            anguloinicial,
            angulodeseado,
            #frecuencia,
            ])
        )
        datacompartidos(e)

        page.add(ft.Column([ft.ElevatedButton(text="Calcular Factor Potencia", on_click=calcular)]))





    page.add(ft.Column([
        ft.ElevatedButton(text=" Calcular Factor Potencia de un Motor", on_click=factorPotenciaMotor),
            ])
        )










if __name__ == '__main__':
    ft.app(target=main)