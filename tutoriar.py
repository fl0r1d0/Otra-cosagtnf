# Importamos las librerías necesarias
import random
import requests

# Definimos la clase Sarco que hereda de la clase object
class Sarco(object):

  # Definimos el método constructor que recibe el nombre del personaje
  def __init__(self, name):
    # Asignamos el nombre al atributo name
    self.name = name
    # Asignamos una lista de palabras coloquiales, vulgares y despectivas al atributo words
    self.words = ["gilipollas", "imbécil", "idiota", "estúpido", "tonto", "mierda", "basura", "asco", "caca", "pedo"]
    # Asignamos una lista de expresiones ingeniosas, ocurrentes y divertidas al atributo expressions
    self.expressions = ["¡Qué divertido!", "¡Qué casualidad!", "¡Qué injusticia!", "¡Qué iluso!", "¡Qué pena!", "¡Qué risa!", "¡Qué horror!", "¡Qué asco!", "¡Qué sorpresa!", "¡Qué aburrimiento!"]
    # Asignamos una lista de temas sobre los que burlarse al atributo topics
    self.topics = ["el día", "la película", "el chico", "el trabajo", "el estado de ánimo", "la vida", "la muerte", "la política", "la religión", "el amor"]
    # Asignamos una lista de frases sarcásticas sobre cada tema al atributo sentences
    self.sentences = [
      ["¿Qué tal el día? ¿Te has tropezado con alguna piedra o te has caído por las escaleras?", 
      "¿Qué tal el día? ¿Has visto el sol o te has quedado encerrado en tu cueva?", 
      "¿Qué tal el día? ¿Has hecho algo interesante o has perdido el tiempo como siempre?"],
      ["¿Qué haces mirando esa película tan aburrida? ¿No prefieres ver algo más interesante como un documental sobre la muerte o un programa sobre torturas medievales?", 
      "¿Qué haces mirando esa película tan aburrida? ¿No te das cuenta de que es una mentira y que todo es falso?", 
      "¿Qué haces mirando esa película tan aburrida? ¿No tienes nada mejor que hacer con tu vida?"],
      ["¿Qué te parece ese chico tan guapo que te gusta? ¿Sabes que tiene novia y que además es tu prima? ¡Qué casualidad!", 
      "¿Qué te parece ese chico tan guapo que te gusta? ¿Sabes que es un narcisista y que solo quiere usarte?", 
      "¿Qué te parece ese chico tan guapo que te gusta? ¿Sabes que es gay y que le gustas tú?"],
      ["¿Qué tal tu trabajo? ¿Te pagan bien por hacer el vago o te explotan como a un esclavo? ¡Qué injusticia!", 
      "¿Qué tal tu trabajo? ¿Te gusta lo que haces o lo odias con toda tu alma? ¡Qué pena!", 
      "¿Qué tal tu trabajo? ¿Te sientes realizado o frustrado? ¡Qué risa!"],
      ["¿Qué te pasa? ¿Estás triste o enfadado? ¿No te das cuenta de que la vida es una broma cruel y que no vale la pena tomársela en serio? ¡Qué iluso!", 
      "¿Qué te pasa? ¿Estás feliz o contento? ¿No te das cuenta de que la felicidad es efímera y que pronto vendrá la desgracia? ¡Qué horror!", 
      "¿Qué te pasa? ¿Estás nervioso o asustado? ¿No te das cuenta de que el miedo es irracional y que solo te limita? ¡Qué asco!"],
      ["¿Qué opinas de la vida? ¿Te parece un regalo o una maldición? ¡Qué sorpresa!", 
      "¿Qué opinas de la vida? ¿Te parece una aventura o una rutina? ¡Qué aburrido"],
      ["¿Qué opinas de la muerte? ¿Te da miedo o te da igual? ¡Qué divertido!", 
      "¿Qué opinas de la muerte? ¿Te parece el final o el principio? ¡Qué casualidad!", 
      "¿Qué opinas de la muerte? ¿Te parece una liberación o una condena? ¡Qué injusticia!"],
      ["¿Qué opinas de la política? ¿Te parece una farsa o una necesidad? ¡Qué iluso!", 
      "¿Qué opinas de la política? ¿Te interesa o te aburre? ¡Qué pena!", 
      "¿Qué opinas de la política? ¿Te involucras o te abstienes? ¡Qué risa!"],
      ["¿Qué opinas de la religión? ¿Te parece una creencia o una superstición? ¡Qué horror!", 
      "¿Qué opinas de la religión? ¿Te ayuda o te perjudica? ¡Qué asco!", 
      "¿Qué opinas de la religión? ¿Te convence o te cuestiona? ¡Qué sorpresa!"],
      ["¿Qué opinas del amor? ¿Te parece una ilusión o una realidad? ¡Qué aburrimiento!", 
      "¿Qué opinas del amor? ¿Te hace feliz o te hace sufrir? ¡Qué divertido!", 
      "¿Qué opinas del amor? ¿Te enamoras o te desenamoras? ¡Qué casualidad!"]
    ]
    # Asignamos un diccionario vacío al atributo memory
    self.memory = {}

  # Definimos el método speak que recibe el nombre de la persona a la que se dirige
  def speak(self, person):
    # Elegimos un tema al azar de la lista topics
    topic = random.choice(self.topics)
    # Elegimos una frase al azar de la lista sentences según el tema elegido
    sentence = random.choice(self.sentences[self.topics.index(topic)])
    # Elegimos una palabra al azar de la lista words
    word = random.choice(self.words)
    # Elegimos una expresión al azar de la lista expressions
    expression = random.choice(self.expressions)
    # Formamos el mensaje con el nombre de la persona, la frase, la palabra y la expresión
    message = f"Hola, {person}. {sentence} Eres un {word}. {expression}"
    # Imprimimos el mensaje por pantalla
    print(message)
    # Guardamos el mensaje en el diccionario memory con la clave person
    self.memory[person] = message

  # Definimos el método learn que recibe el nombre de la persona y el mensaje que le envía
  def learn(self, person, message):
    # Usamos la librería requests para enviar una petición a una API que analiza el sentimiento del mensaje
    response = requests.post("https://api.sentimll.com/v1", json={"text": message})
    # Obtenemos el resultado del análisis en formato JSON
    result = response.json()
    # Obtenemos el valor del sentimiento del mensaje, que puede ser positivo, negativo o neutro
    sentiment = result["result"]["sentiment"]
    # Si el sentimiento es positivo, respondemos con un mensaje sarcástico y negativo
    if sentiment == "positive":
      reply = f"¡Qué bien! Me alegro mucho por ti. ¡Notese el sarcasmo!"
    # Si el sentimiento es negativo, respondemos con un mensaje burlón y positivo
    elif sentiment == "negative":
      reply = f"¡Qué mal! Lo siento mucho por ti. ¡Notese la ironía!"
    # Si el sentimiento es neutro, respondemos con un mensaje indiferente y aburrido
    else:
      reply = f"¡Qué más da! No me importa nada lo que me digas. ¡Notese el desdén!"
    # Imprimimos la respuesta por pantalla
    print(reply)
