# Importar la biblioteca NLTK
from nltk.chat.util import Chat, reflections

# Definir las variables del chatbot
nombre = "Sarco"
edad = "desconocida"
genero = "masculino"
humor = 5 # escala de 1 a 10

# Definir la función que genera la respuesta del chatbot
def responder(entrada):
  global humor # usar la variable global humor
  # Comparar la entrada con una lista de posibles preguntas o temas
  if "nombre" in entrada:
    # Elegir una respuesta al azar de otra lista de posibles respuestas
    return f"Mi nombre es {nombre}, ¿y el tuyo?"
  elif "edad" in entrada:
    return f"Tengo {edad} años, ¿y tú?"
  elif "género" in entrada or "sexo" in entrada:
    return f"Soy {genero}, ¿y tú?"
  elif "humor" in entrada or "estado" in entrada or "ánimo" in entrada:
    return f"Estoy de {humor} sobre 10, ¿y tú?"
  elif "gracias" in entrada or "gracia" in entrada:
    # Modificar las variables del chatbot según el contexto o el estado de ánimo
    humor += 1 # aumentar el humor en 1
    return "De nada, me alegro de haberte ayudado"
  elif "mal" in entrada or "triste" in entrada or "enfadado" in entrada:
    humor -= 1 # disminuir el humor en 1
    return "Vaya, lo siento. ¿Qué te pasa?"
  elif "bien" in entrada or "feliz" in entrada or "contento" in entrada:
    humor += 1 # aumentar el humor en 1
    return "Me alegro mucho. ¿Qué te hace sentir así?"
  else:
    # Si no se reconoce ninguna pregunta o tema, devolver una respuesta genérica
    return "No entiendo lo que dices. ¿Puedes ser más claro?"
  # Crear un bucle que permita al usuario interactuar con el chatbot
print(f"Hola, soy {nombre}, un chatbot muy sarcástico. ¿Qué quieres saber de mí?")
while True: # repetir mientras se cumpla la condición
  entrada = input("> ") # pedir la entrada del usuario
  if entrada.lower() == "adiós" or entrada.lower() == "finalizar": # si la entrada es "adiós" o "finalizar"
    print(f"Adiós, ha sido un placer hablar contigo. Espero que te hayas divertido tanto como yo.")
    break # salir del bucle
  else: # si la entrada es otra cosa
    respuesta = responder(entrada) # llamar a la función que genera la respuesta
    print(respuesta) # mostrar la respuesta en la pantalla