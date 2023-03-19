archivo2=open("employees.txt","r",encoding="utf8")
texto=archivo2.read().replace("Gestión de operaciones","Gestión-Operaciones").replace("Gestión Humana","Gestión-Humana")

numeros=["1","2","3","4","5","6","7","8","9","0"]
#Crearemos una lista de listas
Empleados=texto.split("\n")
N25=int((len(Empleados)*0.25))
N75=int((len(Empleados)*0.75))
Empleados.pop(0)
ListaEmpleados=[]
#Ordenaremos a los empleados por su salario de menor a mayor
for empleado in Empleados:
    listaValores=empleado.split(" ")
    listaValores.reverse()
    salario=int(listaValores[0])
    listaValores[0]=salario
    ListaEmpleados.append(listaValores)
ListaEmpleados.sort()
def convertidorNumeros(n):
    numero=str(n)
    contador=0
    pila = deque()
    for i in range(len(numero)-1,-1,-1):
        if numero[i]=="0":
            contador=contador+1
        pila.append(numero[i])
        if contador==3:
            pila.append(".")
            contador=0
    convertido=""
    while(len(pila)!=0):
        convertido=convertido+pila.pop()
    return convertido











