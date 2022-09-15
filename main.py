import time  # Importamos la librería time
import random as rd  # Importamos la librería random
import random

puntaje = 0
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
load = '||'

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print("¡Hey! Te doy la bienvenida a mi trivia sobre la ciudad de Lima.")
print(" => Pondremos a prueba tus conocimientos.\n")

while iniciar_trivia == True:  #  Mientras iniciar_trivia sea True, repite:
    intentos += 1
    puntaje = 0
    input(CYAN + "Presiona Enter para continuar \n" + RESET)
    ### Loading...###
    print('CARGANDO TRIVIA')
    for i in range(0, 6):
        print('{}%'.format(i * 20) + i * load + '..' * (5 - i), end='\r')
        time.sleep(1)
    print('\n')
    ################

    print("\nIntento número:", intentos)

    nombre = input(BLUE + "\nIngresa tu nombre: " + RESET)
    nombre = str.capitalize(nombre)

    print(
        "\nHola" + GREEN, nombre, RESET +
        "recuerda que después de responder cada pregunta, debes presionar 'Enter' para enviar tu respuesta:"
    )
    time.sleep(2)  # Espera 2 segundo antes de continuar.

    print(MAGENTA + "\n => Actualmente tienes:", puntaje,
          "puntos acumulados.\n" + RESET)

    ### PREGUNTA 1 ###
    time.sleep(4)  # Espera 4 segundo antes de continuar.
    print("1) ¿En qué año se fundó la ciudad de Lima?")
    print("   a) 1530")
    print("   b) 1535")
    print("   c) 1532")
    print("   d) 1533")

    respuesta_1 = input("\nTu respuesta: ").lower()

    while respuesta_1 not in ("a", "b", "c", "d", "x"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_1 == "b":
        puntajer = random.randint(5, 8)
        puntaje += puntajer
        print(
            GREEN +
            "\n=> ¡Respuesta correcta! Lima se fundó el 18 de enero de 1535. \n"
            + RESET)
        print(YELLOW + " => ¡Ganaste", puntajer, "puntos!\n" + RESET)
        print(YELLOW + " => Actualmente tienes:", puntaje, "puntos.\n" + RESET)
    elif respuesta_1 == "x":
        puntaje += 5
        print(BLUE + " => ¡Abriste un bono sorpresa!", nombre,
              "Ganaste 5 puntos.\n" + RESET)
    else:
        puntaje -= 2.5
        print(
            RED +
            "\n => Respuesta incorrecta (Lima se fundó el 18 de enero de 1535). \n"
            + RESET)
        print(YELLOW + " => ¡Perdiste 2.5 puntos!\n" + RESET)
        print(YELLOW + " => Actualmente tienes:", puntaje, "puntos.\n" + RESET)

    ### Pregunta 2 ###
    time.sleep(4)  # Espera 4 segundo antes de continuar.
    print("2) ¿Cuál es la huaca más antigua de la ciudad de Lima?")
    print("   a) Huaca Pucllana")
    print("   b) Huaca Huallamarca")
    print("   c) Huaca Paraíso")
    print("   d) Huaca Puruchuco")

    respuesta_2 = input("\nTu respuesta: ").lower()

    while respuesta_2 not in ("a", "b", "c", "d", "y"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_2 == "a":
        puntaje -= 2.5
        print(RED + " => ¡Incorrecto!", nombre,
              "La Huaca Pucllana no es la más antigua de Lima.\n" + RESET)
        print(YELLOW + " => ¡Perdiste 2.5 puntos!\n" + RESET)
        print(YELLOW + " => Actualmente tienes:", puntaje, "puntos.\n" + RESET)

    elif respuesta_2 == "b":
        puntaje -= 2.5
        print(RED + " => ¡Incorrecto!", nombre,
              "La Huaca Huallamarca no es la más antigua de Lima.\n" + RESET)
        print(YELLOW + " => ¡Perdiste 2.5 puntos!\n" + RESET)
        print(YELLOW + " => Actualmente tienes:", puntaje, "puntos.\n" + RESET)

    elif respuesta_2 == "d":
        puntaje -= 2.5
        print(RED + " => ¡Incorrecto!", nombre,
              "La Huaca Puruchuco no es la más antigua de Lima.\n" + RESET)
        print(YELLOW + " => ¡Perdiste 2.5 puntos!\n" + RESET)
        print(YELLOW + " => Actualmente tienes:", puntaje, "puntos.\n" + RESET)
    elif respuesta_2 == "y":
        puntaje += 5
        print(BLUE + " => ¡Abriste un bono sorpresa!", nombre,
              "Ganaste 5 puntos.\n" + RESET)

    else:
        puntajer = random.randint(5, 10)
        puntaje += puntajer
        print(
            GREEN + "\n =>", nombre,
            "¡Respuesta correcta! La Huaca Paraíso o Chuquitanta es la más antigua de la ciudad, y se encuentra en el distrito de San Martín de Porres.\n"
            + RESET)
        print(YELLOW + " => ¡Ganaste", puntajer, "puntos!\n" + RESET)
        print(YELLOW + " => Actualmente tienes:", puntaje, "puntos.\n" + RESET)

    ### PREGUNTA 3 ####
    time.sleep(4)  # Espera 4 segundo antes de continuar.
    print("3) ¿Cuál es la flor representativa de la ciudad de Lima?")
    print("   a) La rosa")
    print("   b) La flor de Amancaes")
    print("   c) La cantuta")
    print("   d) La retama")
    respuesta_3 = input("\nTu respuesta: ").lower()

    while respuesta_3 not in ("a", "b", "c", "d", "z"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: "
        ).lower()

    if respuesta_3 == "b":
        puntaje = puntaje + 20
        print(
            GREEN +
            "\n => ¡Respuesta correcta! La flor de amancaes crece en los valles de Lima. Es de color amarillo intenso y florece en el invierno.  \n"
            + RESET)
        print(YELLOW + " => ¡Ganaste 20 puntos!\n" + RESET)

    elif respuesta_3 == "z":
        puntaje += 5
        print(BLUE + " => ¡Abriste un bono sorpresa!", nombre,
              "Ganaste 5 puntos.\n" + RESET)

    else:
        puntaje -= 2.5
        print(
            RED +
            "\n => ¡Respuesta incorrecta! (La flor de amancaes es la flor típica y simbolica de Lima). \n"
            + RESET)
        print(YELLOW + " => ¡Perdiste 2.5 puntos!" + RESET)

    print("\n ##### Gracias por participar", nombre, "#####")
    time.sleep(2)  # Espera 2 segundo antes de continuar.
    start_time = time.time()
    elapsed_time = 0
    print('\n' + MAGENTA + 'Tu puntaje final es:')

    while elapsed_time < 3:
        #print('{}'.format(rd.randint(0,10)), end='\r')
        print(rd.randint(0, 20), end='\r')
        end_time = time.time()
        elapsed_time = end_time - start_time

    print('{:.1f}'.format(puntaje), end='\r')
    print('\n')

    print(GREEN + "\n¿Deseas intentar la trivia nuevamente?" + RESET)
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla  más 'Enter' para finalizar: \n"
    ).lower()

    if repetir_trivia != "si":  # != significa "distinto"
        print("\n     Espero ", nombre,
              " que lo hayas pasado bien, ¡hasta pronto!")
        iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
