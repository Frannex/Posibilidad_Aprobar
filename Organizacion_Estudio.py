import os
import time
import datetime

# Función para limpiar la pantalla
def limpiar_pantalla():
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')  # Comando para borrar pantalla

# Función de mostrar mensaje con animación
def mostrar_mensaje(texto):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.01)
    print()

# Función para preguntar la materia a estudiar
def materia_preguntar():
    while True:
        materia = input("¿Qué materia tienes que estudiar? ")
        if not materia.isnumeric(): #Comprobrar que este escrito en letra
            return materia
        else:
            mostrar_mensaje("¡ERROR!")
            mostrar_mensaje("¡DEBES ESCRIBIR EL TEXTO EN LETRAS!")

# Función para preguntar en qué día hay que estudiar la materia
def dias_estudio(materia):
    while True:
        estudiar_materia = input("¿En qué día tienes que estudiar para " + str(materia) + "? (YYYY-MM-DD) ")
        try:
            fecha_estudio = datetime.datetime.strptime(estudiar_materia, "%Y-%m-%d") #Para que escriba el año, mes y dia (Podes cambiarlo si quieres)
            return fecha_estudio
        except ValueError: #Para que cuando te tire error si digitaste mal no aparezca cualquier error y aparezca lo que vos queres
            print("Error: Formato de fecha incorrecto. Introduce la fecha en el formato solicitado (YYYY-MM-DD).".upper())

# Función para saber en qué día quieres estudiar
def dias_querer_estudiar(materia):
    while True:
        querer_estudiar = input("¿En qué día quieres estudiar para " + str(materia) + "? (YYYY-MM-DD) ")
        try:
            fecha_estudio = datetime.datetime.strptime(querer_estudiar, "%Y-%m-%d")
            return fecha_estudio
        except ValueError:  #Para que cuando te tire error si digitaste mal no aparezca cualquier error y aparezca lo que vos queres
            print("Error: Formato de fecha incorrecto. Introduce la fecha en el formato solicitado (YYYY-MM-DD).".upper())

#Función para restar días
def dias_restantes(estudiar_materia,querer_estudiar):
    dias_restar=(estudiar_materia-querer_estudiar).days #Para que no aparezca hora ni nada
    if dias_restar>=0:
        mostrar_mensaje("Faltan " + str(dias_restar) + " dias para el examen.")
        return dias_restar
    else:
        mostrar_mensaje("¡ERROR DE PROGRAMA")
        mostrar_mensaje("IMPOSIBLE CALCULAR DIAS NEGATIVOS. ¡INTENTE NUEVAMENTE!")
        exit()#cerrar programa
#Funcion para calcular un porcentaje de aprobacion o no
def calcular_porcentaje_estudio(dias_restar):
    if dias_restar < 1: #porcentaje si te queda menos de un dia de estudio
        porcentaje = 2.5  
        mostrar_mensaje("¡Reza para que te vaya bien!")
        mostrar_mensaje("Recomendación: Tuviste que haberte puesto a estudiar unos dias antes.")
    elif dias_restar < 2:
        porcentaje = 14.7
        mostrar_mensaje("Tienes pocas posibilidad de aprobar :(")
        mostrar_mensaje("Recomendación: Dos dias no es suficiente para estudiar, así que estudia las proximas 24/7.")
        
    elif dias_restar < 3:
        porcentaje = 35.9
        mostrar_mensaje("Puede que te vaya bien")
        mostrar_mensaje("Recomendación: Repasa antes de arrancar la prueba.")
        
    elif dias_restar < 4:
        porcentaje = 67.3
        mostrar_mensaje("Sin dudas fuiste listo")
        mostrar_mensaje("Recomendación: Repasa todos los dias un rato y ya lo tendras.")
    elif dias_restar < 5:
        porcentaje = 75.9
        mostrar_mensaje("Tienes altas posibilidades de aprobar para el examen!")
        mostrar_mensaje("Recomendación: Tomatelo con calma, tienes 5 dias.")
    elif dias_restar < 6:
        porcentaje = 89.3
        mostrar_mensaje("Vas a aprobar, quedate tranqui")
        mostrar_mensaje("Recomendación: Tomate unos matesitos, ya la tenes.")
    elif dias_restar < 7:
        porcentaje = 95.4
        mostrar_mensaje("Minimo un 8 tenes que sacarle loquita")
        mostrar_mensaje("Recomendación: Ya la tene mi loco.")
    else:
        porcentaje = 100  # Porcentaje de estudio si quedan más de 7 dias para estudiar
        mostrar_mensaje("Si no aprobas, es porque sos tremendo salame")
        mostrar_mensaje("Recomendación: No te puedo recomendar nada, hace MUCHISIMOS dias que estas estudiando.")
    return porcentaje

# Función para preguntar si desea obtener información sobre otra materia
def preguntar_otra_materia():
    while True:
        opcion = input("¿Deseas obtener información sobre otra materia? (S/N): ")
        if opcion.upper() == 'S':
            return True
        elif opcion.upper() == 'N':
            mostrar_mensaje("¡Gracias por haber usado el programa!")
            mostrar_mensaje("¡Hasta luego!")
            return False
        else:
            mostrar_mensaje("Opción inválida. Por favor, ingresa 'S' para sí o 'N' para no.")


# Estructura del programa
def ejecutar_programa():
    while True:
        limpiar_pantalla()
        materia = materia_preguntar()
        fecha_estudio = dias_estudio(materia)
        fecha_querer_estudiar = dias_querer_estudiar(materia)
        dias_restantes_valor = dias_restantes(fecha_estudio, fecha_querer_estudiar)
        porcentaje_estudio = calcular_porcentaje_estudio(dias_restantes_valor)
        mostrar_mensaje("Posibilidad de aprobar el examen: " + str(porcentaje_estudio) + "%") #Muestra la posibilidad que tienes de aprobar el examen

        if not preguntar_otra_materia():
            break
# Ejecución del programa
ejecutar_programa()
