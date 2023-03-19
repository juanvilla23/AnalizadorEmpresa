from PreparacionDatos import *
Marketig=[]
Tecnología=[]
Finanzas=[]
GestiónOperaciones=[]
GestiónHumana=[]
if __name__=="__main__":
#separamos los empleados por departamento
    print(ListaEmpleados)
    for empleado in ListaEmpleados:
        if empleado[1]=="Marketig":
            Marketig.append(empleado)
        if  empleado[1]=="Tecnología":
            Tecnología.append(empleado)
        if empleado[1] == "Finanzas":
            Finanzas.append(empleado)
        if empleado[1]=="\"Gestión-Operaciones\"":
            GestiónOperaciones.append(empleado)
        if empleado[1]=="\"Gestión-Humana\"":
            GestiónHumana.append(empleado)
N25Marketig=int((len(Marketig)*0.25)-1)
N75Marketig=int((len(Marketig)*0.75)-1)
print(f"Numero de Personas en Marketig: {len(Marketig)}")
print(f" Numero de Salarios Minimos: {N25Marketig+1}")
print(f" Numero de Salarios Maximos: {len(Marketig)-N75Marketig}")
print("Maximo y minimos de el Departamento de Gestión-Humana: ")
i=0
while i<=N25Marketig:
    empleado=Marketig[i]
    print(f"Empleado:{empleado[3]} {empleado[2]} / Salario: {empleado[0]} / Departamento: {empleado[1]}")
    i=i+1
ValorNominaMensual=0
for empleado in Marketig:
    ValorNominaMensual=ValorNominaMensual+empleado[0]
ValorNominaAnual=ValorNominaMensual*12
print(f"El valor de la Nomina Mensual en Marketing es: {ValorNominaMensual}")
print(f"El valor de la Nomina Anual en Marketing es: {ValorNominaAnual}")





