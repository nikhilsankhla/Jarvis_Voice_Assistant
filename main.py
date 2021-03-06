import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice" , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello Sweety, I am Jarvis")


def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print("User said: ",query)
        speak("User Said")
        speak(query)

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    res=0
    while res==0:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open ok website" in query:
            webbrowser.open("ok.xxx")
        elif "open google " in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            music_dir = "C:\\Users\\pc\\Music\\Playlists"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("The Time is " + strTime)
            speak("Sir the Time is "+ strTime)
        elif "on youtube" in query:
            song = query.replace("play","")
            speak("Playing " + song)
            pywhatkit.playonyt(song)








