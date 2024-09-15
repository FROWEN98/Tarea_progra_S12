# Declaramos nuestra lista 3D
temperatura = [
    [  # matriz ciudad 1
        [22, 10, 15, 17, 16, 18, 21],
        [14, 18, 19, 20, 21, 22, 26],
        [15, 17, 17, 21, 24, 26, 28],
        [15, 16, 18, 22, 24, 28, 18]
    ],
    [  # matriz ciudad 2
        [25, 26, 21, 27, 29, 24, 26],
        [25, 23, 26, 21, 19, 20, 14],
        [24, 25, 26, 23, 21, 22, 25],
        [21,25,26,23,21,27,19,18,17]
    ],
    [  # matriz ciudad 3
        [25, 23, 21, 25, 14, 29, 25],
        [27, 22, 27, 30, 12, 15, 21],
        [32, 21, 31, 22, 25, 27, 25],
        [21,25,24,28,29,17,16,15,31]
    ]
]

# Declaramos variables de la ciudad y la semana que queremos saber el promedio







# Usar bucles for anidados para calcular el promedio
def temperaturas (temperatura,c,s):

    #Creamos un  for en el cual vamos a recorrer
    suma = 0 # Declaramos nuestra variable y la inicializamos en 0
    for i in range (len(temperatura[c][s])):
        suma+= temperatura[c][s][i]   #Sumamos nuestra lista con la iteración i que va a recorrer cada temperatura

    prom = suma / len(temperatura[c][s]) # Dividimos  nuestra suma para la longitud de la semana que escojimos en este caso para 7

    return prom # Retornamos el promedio

#Declaramos 2 variables para llamar por teclado a la ciudad y semana

ciu = int(input("Ingrese la ciudad (0 a 2) : "))
sem = int(input("Ingrese la semana  (0 a 3) : "))


while ciu > 2 and sem > 3 :  #Creamos un bucle while que va a decirnos que volvamos a ingresar si colocamos un indice que no hay
    print("Vuelva a ingresar")
    ciu = int(input("Ingrese la ciudad (0 a 2) : "))
    sem = int(input("Ingrese la semana  (0 a 3) : "))

#Llamamos a nuestra funcion
prom_final = (temperaturas(temperatura,ciu,sem))
print(f"La ciudad {ciu} en su semana {sem} tiene un promedio de {prom_final} grados") #Imprimimos en pantalla