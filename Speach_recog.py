import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    re = sr.Recognizer()
    with sr.Microphone() as sor:
        print("Listening....")
        re.pause_threshold = 1
        audio = re.listen(sor)
    try:
        print("Recognizing....")
        quer = re.recognize_google(audio,language='en-GB')
        print(quer)

    except Exception as e:
        print(e)
        speak("Please Repeat again...")

        return "None"
    return quer
takeCommand()