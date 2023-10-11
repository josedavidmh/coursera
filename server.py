# Importamos los paquetes de flask para desplegar en la web
from flask import Flask,render_template,request
# Importamos el modulo creado para la detección de emociones
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def emotion_detec():
    """Funcion que recibe un texto por get para analizar la emoción que transmite
       emotion_detec()
       retorna la emoción dominante.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)
    if dominant_emotion is None:
        return "Texto invalido, intente nuevamente"
    else:
        return "La respuesta es: {}.".format(dominant_emotion)

@app.route("/")
def render_index_page():
    """
    Retorna la pagina principal en html.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5001)