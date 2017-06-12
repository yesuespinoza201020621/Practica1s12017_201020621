from os import system
system("cls")
matriz=[]
matriz2=[]
matriz3=[]
resta=0
res=[]
res2=[]
res3=[]
suma=0
val=0
val1=0
n=[0,1,1,1,1,1,1,1,1]
val2=-1
print(n)
x1=2
y2=3
matriz4 = [[1]*x1 for i in xrange(y2)]

def print_r(matriz4):
    for fila in matriz4:
        print fila

def transpuesta(matriz4):
    rows = len(matriz4)
    cols = len(matriz4[0])
    return [[matriz4[j][i] for j in xrange(rows)] for i in xrange(cols)]

print "Original"
print(matriz4)




while True:
	print("Bienvenido:")
	menu=input("Si deseas ingresar: 1[MatrizxEscalar], 2[suma o resta de matriz], 3[Salir]: ")

	if menu==1:

		for i in range(10):
			a=input("Introduce la matriz: ")
			matriz3.append(a)
		for i in n:
			val2+=i
			suma=((matriz3[val2]))
			res3.append(suma)
            
		print(res3)

	if menu==2:
		for i in range(5):
			x=input("Introduce el primer numero:" )
			y=input("Introduce el primer numero de la segunda matriz:")
			matriz.append(x)
			matriz2.append(y)
		print(matriz)
		print(matriz2)

		while True:
			opcion= input("Introduce: [1]Suma, [2] resta, [3]Salir:  ")
			if opcion==1:
				for i in n:
					val+=i
					suma= matriz2[val]+matriz[val]
					res.append(suma)
				print("la matriz resultante fue:"+str(res) )
			elif opcion==2:
				for i in n:
					val1+=i
					resta= matriz2[val]-matriz[val]
					res2.append(resta)
				print("la matriz resultante fue:"+str(res2) )
			elif opcion==3:
				break
	elif menu==3: break



"""
x1=3
y2=3
n=x1*y2
a=[[1,2,3],[7,4,5]]



matriz = [[1]*x1 for i in xrange(y2)]

def print_r(matriz):
    for fila in matriz:
        print fila

def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    return [[matriz[j][i] for j in xrange(rows)] for i in xrange(cols)]

print "Original"
print_r(matriz)
print "TRANSPUESTA"
print_r(transpuesta(matriz))
print_r(a)
"""
