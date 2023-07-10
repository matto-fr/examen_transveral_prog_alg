import os
os.system("cls")
import numpy as np

Menu = '''
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
'''
Menu_Entradas = '''
- Platinum: $120.000 (Asientos del 1 al 20)
- Gold:     $80.000  (Asientos del 21 al 50)
- Silver:   $50.000  (Asientos del 51 al 100)'''

lista_ubicaciones = np.arange(1,11)
lista_ubicaciones2 = np.arange(11,21)
lista_ubicaciones3 = np.arange(21,31)
lista_ubicaciones4 = np.arange(31,41)
lista_ubicaciones5 = np.arange(41,51)
lista_ubicaciones6 = np.arange(51,61)
lista_ubicaciones7 = np.arange(61,71)
lista_ubicaciones8 = np.arange(71,81)
lista_ubicaciones9 = np.arange(81,91)
lista_ubicaciones10 = np.arange(91,101)
lista_asistentes = []

cont_platinum = 0
cont_gold = 0
cont_silver = 0
total_platinum = 0
total_gold = 0
total_silver  = 0
total_precio = total_platinum + total_gold + total_silver
total_cantidad = cont_platinum + cont_gold + cont_silver
run_persona = 0
i = 0

def comprar_ent():
    global cont_platinum, cont_gold, cont_silver, total_platinum, total_gold, total_silver, total_precio, total_cantidad
    global run_persona, i
    while True:
        try:
            cantidad_ent = int(input("¿Cuántas entradas desea comprar?\n"))
            if cantidad_ent < 1 or cantidad_ent > 3:
                print("Error, la cantidad de entradas a comprar deben ser al menos 1 y máximo 3")
            elif cantidad_ent >= 1 and cantidad_ent <= 3:
                print(Menu_Entradas)
                print(f'''
     ESCENARIO
{lista_ubicaciones}
{lista_ubicaciones2}
{lista_ubicaciones3}
{lista_ubicaciones4}
{lista_ubicaciones5}
{lista_ubicaciones6}
{lista_ubicaciones7}
{lista_ubicaciones8}
{lista_ubicaciones9}
{lista_ubicaciones10}
''')
                for i in range(cantidad_ent):
                    seleccion_ent = int(input("Seleccione el número de la entrada que desea comprar\n"))
                    while True:
                        try:
                            if seleccion_ent == lista_ubicaciones.size > 0 [lista_ubicaciones == "x"] or\
                            seleccion_ent == lista_ubicaciones2.size > 0 [lista_ubicaciones2 == "x"] or\
                            seleccion_ent == lista_ubicaciones3.size > 0 [lista_ubicaciones3 == "x"] or\
                            seleccion_ent == lista_ubicaciones4.size > 0 [lista_ubicaciones4 == "x"] or\
                            seleccion_ent == lista_ubicaciones5.size > 0 [lista_ubicaciones5 == "x"] or\
                            seleccion_ent == lista_ubicaciones6.size > 0 [lista_ubicaciones6 == "x"] or\
                            seleccion_ent == lista_ubicaciones7.size > 0 [lista_ubicaciones7 == "x"] or\
                            seleccion_ent == lista_ubicaciones8.size > 0 [lista_ubicaciones8 == "x"] or\
                            seleccion_ent == lista_ubicaciones9.size > 0 [lista_ubicaciones9 == "x"] or\
                            seleccion_ent == lista_ubicaciones10.size > 0 [lista_ubicaciones10 == "x"]:
                                print("Error, esa ubicación ya ha sido comprada")                   
                            if seleccion_ent < 1 or seleccion_ent > 100:
                                print("Error, el n° de la entrada debe estar entre 1 y 100")
                            elif seleccion_ent >= 1 and seleccion_ent <= 100:
                                run_persona = int(input("Digite el run del asistente: "))
                                lista_asistentes.append(run_persona)
                                if seleccion_ent >= 1 and seleccion_ent <= 20:
                                    cont_platinum += 1
                                    total_platinum += 120000
                                    if seleccion_ent >= 1 and seleccion_ent <= 10:
                                        lista_ubicaciones[lista_ubicaciones == seleccion_ent] = "x"
                                    elif seleccion_ent >= 11 and seleccion_ent <= 20:
                                        lista_ubicaciones2[lista_ubicaciones2 == seleccion_ent] = "x"
                            elif seleccion_ent >= 21 and seleccion_ent <= 50:
                                cont_gold += 1
                                total_gold += 80000
                                if seleccion_ent >= 21 and seleccion_ent <= 30:
                                    lista_ubicaciones3[lista_ubicaciones3 == seleccion_ent] = "x"
                                elif seleccion_ent >= 31 and seleccion_ent <= 40:
                                    lista_ubicaciones4[lista_ubicaciones4 == seleccion_ent] = "x"
                                elif seleccion_ent >= 41 and seleccion_ent <= 50:
                                    lista_ubicaciones5[lista_ubicaciones5 == seleccion_ent] = "x"
                            elif seleccion_ent >= 51 and seleccion_ent <= 100:
                                cont_silver += 1
                                total_silver += 50000
                                if seleccion_ent >= 51 and seleccion_ent <= 60:
                                    lista_ubicaciones6[lista_ubicaciones6 == seleccion_ent] = "x"
                                elif seleccion_ent >= 61 and seleccion_ent <= 70:
                                    lista_ubicaciones7[lista_ubicaciones7 == seleccion_ent] = "x"
                                elif seleccion_ent >= 71 and seleccion_ent <= 80:
                                    lista_ubicaciones8[lista_ubicaciones8 == seleccion_ent] = "x"
                                elif seleccion_ent >= 81 and seleccion_ent <= 90:
                                    lista_ubicaciones9[lista_ubicaciones9 == seleccion_ent] = "x"
                                elif seleccion_ent >= 91 and seleccion_ent <= 100:
                                    lista_ubicaciones10[lista_ubicaciones10 == seleccion_ent] = "x"
                            print("La operación se ha realizado correctamente")
                            break
                        except:
                               print("excepción")
                break
        except:
            print("Se ha producido una excepción")

def mostar_ubi():
    global cont_platinum, cont_gold, cont_silver, total_platinum, total_gold, total_silver, total_precio, total_cantidad
    print(f'''
     ESCENARIO
{lista_ubicaciones}
{lista_ubicaciones2}
{lista_ubicaciones3}
{lista_ubicaciones4}
{lista_ubicaciones5}
{lista_ubicaciones6}
{lista_ubicaciones7}
{lista_ubicaciones8}
{lista_ubicaciones9}
{lista_ubicaciones10}
''')

def listado_asist():
    global run_persona
    print(lista_asistentes)

def ganancias_tot():
    global cont_platinum, cont_gold, cont_silver, total_platinum, total_gold, total_silver, total_precio, total_cantidad
    print(f'''
|   Tipo Entrada   |    Cantidad    |    Total    |
Platinum $120.000  |       {cont_platinum} {total_platinum}
Gold     $80.000   |       {cont_gold}     {total_gold}
Silver   $50.000   |       {cont_silver}   {total_silver}
TOTAL              |       {total_cantidad}{total_precio}
''')
    
def salir():
    print('''
Ha salido del sistema.
----------------------
Información software:
- Nombre desarrollador: Matías Fuentes Riffo
- Fecha creación: 10/07/2023
''')

while True:
    try:
        print(Menu)
        opc = int(input("Seleccione el n° correspondiente a la opción que desea ingresar:\n"))
        if opc == 1:
            comprar_ent()
        elif opc == 2:
            mostar_ubi()
        elif opc == 3:
            listado_asist()
        elif opc ==4:
            ganancias_tot()
        elif opc == 5:
            salir()
            break
        else:
            print("Error, la opción seleccionada debe estar entre 1 y 5")
    except:
        print("Se ha producido una excepción")