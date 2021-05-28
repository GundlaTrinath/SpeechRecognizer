import speech_recognition as sr

rec = sr.Recognizer()
#sound = "wespeak.wav"


with sr.Recognizer() as source:
    print("Speak something: ")
    audio = rec.listen(source)

    try:
        text = rec.recognize_google(source)
        print(text)
    except:
        print('not recognized')
