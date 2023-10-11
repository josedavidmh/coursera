from EmotionDetection.emotion_detection import emotion_detector

dominant_emotion = emotion_detector("Odio trabajar muchas horas")
if dominant_emotion is None:
    print("Texto no valido")
else:
    print("La emoción dominante es: {}.".format(dominant_emotion))
