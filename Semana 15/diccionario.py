#Creamos nuestro diccionario en donde vamos a colocar cable - valor
informacion_personal = {"Nombre":"Jorge", "Edad":26,"Ciudad": "Puyo","Email":"jorgesanchez@gmail.com","Profesión": "Medico General"}

#Imprimimos el diccionario actual
print("\nDICCIONARIO ACTUAL \n",informacion_personal)


#Modificamos el valor Ciudad con el metodo update
informacion_personal.update({"Ciudad": "Guayaquil"})



#Agregamos una nueva clave-valor al diccionario que represente la "profesion" de la persona.

informacion_personal.update({'Profesión':'Ingeniero en Sistemas'})

#Verificamos si la clave telefono existe
tlf = input("Ingrese el nombre de la clave que desea buscar: ")  #Pedimos al usuario que ingrese la clave
if tlf not in informacion_personal :  #Si no existe creamos la clave y valor del telefono
    print(f"No existe la clave {tlf} ") #Imrprimimos un mensaje
    num = int(input(f"Ingrese un numero a {tlf}: "))  #Pedimos que ingrese el numero de telefono
    informacion_personal[tlf] = num

else:
    print("Si existe la clave de teléfono")

#Eliminamos la clave edad
del informacion_personal["Edad"]

#Imprimimos el diccionario actualizado
print(f"\n\nDICCIONARIO ACTUALIZADO \n {informacion_personal}")