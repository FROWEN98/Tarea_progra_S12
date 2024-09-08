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
ciudad_input = 2
semana_input = 1



suma = 0
contador = 0

# Usar bucles for anidados para calcular el promedio
for ciudad in range(len(temperatura)):  # Recorremos las ciudades
    if ciudad == ciudad_input:  # Verificamos si es la ciudad seleccionada
        for semana in range(len(temperatura[ciudad])):  # Recorremos las semanas
            if semana == semana_input:  # Verificamos si es la semana seleccionada
                for temperatura in range(len(temperatura[ciudad][semana])):  # Recorremos las temperaturas
                    suma += temperatura[ciudad][semana][temperatura]  # Sumar las temperaturas
                    contador += 1  # Contamos las temperaturas

# Calcular el promedio si nuestro contador es mayor a 0
if contador > 0:
    promedio = suma / contador  #Calculamos el promedio y dividimos para los 7 numero que son
    print(f"La ciudad {ciudad_input } de la semana {semana_input } tiene una temperatura de promedio : {promedio}")
else:
    print("No se puede calcular.")