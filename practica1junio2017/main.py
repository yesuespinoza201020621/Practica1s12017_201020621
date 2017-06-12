
from os import system
system("cls")


from xml.dom import minidom
xmldoc = minidom.parse("archivo.xml");
# obtenemos el atributo line de <message line="...">

itemlist = xmldoc.getElementsByTagName("x")
for i in itemlist:
    print (i.firstChild.nodeValue)
    x=i.firstChild.nodeValue
itemlist = xmldoc.getElementsByTagName("y")
for i in itemlist:
    print (i.firstChild.nodeValue)
    y=i.firstChild.nodeValue
itemlist = xmldoc.getElementsByTagName("operacion")
for i in itemlist:
    print (i.firstChild.nodeValue)



from cola import Cola
from lista_circular_doble_enlazada import ListaCircularDobleEnlazada
Lista=ListaCircularDobleEnlazada()


print("Calculo de Matrices");
print("");
print("1. Crear Usuario");
print("2. Ingresar al Sistema");
print("3. Salir del Programa");
print("");
print("");
Opcion = int(input("Eliga la Opcion: "))


if Opcion == 1:

    print("cuantos Usuario se ingresaran")
    ingreso = int(input(""))


    contador=0
    while (contador<ingreso):
        print("ingrese nombre usuario")
        usuario = raw_input()
        Lista.agregar_final(usuario)

        print("ingrese password")
        password = raw_input()
        print(usuario)
        contador = contador + 1

print("Calculo de Matrices");
print("");
print("1. Crear Usuario");
print("2. Ingresar al Sistema");
print("3. Salir del Programa");
print("");
print("");
Opcion = int(input("Eliga la Opcion: "))


if Opcion == 3:
    print("salir")
if Opcion == 2:
	print("1. Leer Archivo");
	print("2. Resolver Operacion");
	print("3. Operar la Matriz");
	print("4. Mostrar Usuarios");
	print("5. Mostrar Cola");
	print("6. Cerrar Sesion");
Opcion2 = int(input("Eliga la Opcion: "))

if Opcion2==2:
            print("debe cargar Primero el Archivo")


if Opcion2==3:
            print("debe cargar Primero el Archivo")


if Opcion2==4:
    print("usuarios")

if Opcion2==5:
    print("cola")

if Opcion2==6:
        print("ha cerrado Secion");
if Opcion2==1:
        print("leyendo Archivo")
        print("MATRIZ DE")
        print(x)
        print(y)
else:
        print("carracter no valido")

print("1. Leer Archivo");
print("2. Resolver Operacion");
print("3. Operar la Matriz");
print("4. Mostrar Usuarios");
print("5. Mostrar Cola");
print("6. Cerrar Sesion");
Opcion3 = int(input("Eliga la Opcion: "))
if Opcion3==3:
    print("1. Ingresar Dato");
    print("2. Operar transpuesta");
    print("3. Monstrar matriz Original");
    print("4. Mostrar Matriz transpuesta");
    print("5. regresar");
Opcion4 = int(input("Eliga la Opcion: "))

cola=Cola()
cola.push(12)
cola.push(23)
cola.push(56)
cola.push(78)
cola.show()

cola.pop()
cola.pop()

cola.show()




print("*" * 25)
Lista.recorrer_fin_a_inicio()
