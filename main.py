import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour >= 5 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour > 18 and hour < 20:
        speak("Good Evening")
    else:
        speak("Good Night")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User : {query}\n")
    
    except Exception as e:
        print(e)
        print("Could not understand.")
        return "None"
    
    return query

if __name__ == "__main__":
    speak('Hello')
    wishMe()
    speak("what can I do for you?")

    while True:
        query=takeCommand().lower()