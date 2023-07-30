from audioop import ratecv
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from better_profanity import profanity
print("HI I am Tejas  here for You! HOW CAN I HELP YOU?")


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
voiceRate = 145
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # Without this command, speech will not be audible to us


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        speak("HI I am tejas  here for You! HOW CAN I HELP YOU?")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        speak("HI I am Tejas!  here for You! HOW CAN I HELP YOU?")
    else:
        speak("Good evening")
        speak("HI I am tejas  here for You! HOW CAN I HELP YOU?")


def takeCommand():  # It takes microphone input from the user and returns string output
    r = sr.Recognizer()

    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")

        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please... Not recognizable")
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case
        if(profanity.contains_profanity(query)):
             print("Query contains bad word/s")
             exit()
            # Logic for executing tasks based on query
        elif 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif ' youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif ('play music' in query) or ('gana' in query):
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif ('time' in query) or ('samay' in query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif ("my documents" in query) or ('kholo' in query):
            codePath = "C:\\Users\\SHALIN DASHORA\\OneDrive\\Documents"
            os.startfile(codePath)
        elif "pose" in query:
            codePath = "D:\\all programs\\practice\\vect"
            os.startfile(codePath)
        elif "what are you doing" in query:
            speak("Hi,I am here helping you")
