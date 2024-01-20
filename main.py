import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("wait for few Moments....")
        query=r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")

    except Exception as e:
        print(e)
        speak("Please Tell me Again")
        query="none"
    return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        print("Good Morning SAI...")
        speak("Good Morning SAI...")
    elif hour>=12 and hour <17:
        print("Good afternoon SAI...")
        speak("Good afternoon SAI...")
    elif hour>=17 and hour <21:
        print("Good evening SAI...")
        speak("Good evening SAI...")
    else:
        print("Good Night SAI...")
        speak("Good Night SAI...")


if __name__ == "__main__":
    wishings()
    query=commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is {strTime}")


    elif 'open chrome'in query:
        speak ("Opening chrome Aplliction sir...")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'open spotify'in query:
        speak (" opening spotify application sir...")
        os.startfile("C:\\Users\\saida\\AppData\\Roaming\\Spotify\\cache\\hide_window.vbs")

    elif 'wikipedia' in query:
        speak("searching in wikipedia....")
        try:
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia,")
            print(results)
            speak(results)

        except:
            speak("no result found sorry sir...")
            print("no result found sorry sir...")











