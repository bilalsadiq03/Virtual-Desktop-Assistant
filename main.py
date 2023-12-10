import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

paths = {
    'notepad' : 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad',
    'calc' : 'C:\\Program Files (x86)\\Common Files\\System\\shell32.dll,14\\Calculator',
    'vs code' : "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    'music' : "C:\\Users\\DELL\\Music",
    'cmd' : "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt" }

sites = {
    'google' : 'https://www.google.com/search?q=',
    'youtube' : 'https://www.youtube.com/results?search_query=',
    'stackoverflow' : 'https://www.stackoverflow.com/results?search_query=',
    'github' : 'https://www.github.com/',
    'instagram' : 'https://www.instagram.com/',
    'codechef' : "https://www.codechef.com/"

}

def open_cmd():
    os.system('start cmd')

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe ():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak(" Good Evening!")
    speak("I am your virtual assistant. How may i help you.")

def takeCommand():
    #It takes microphone input from user and returns string output.
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("Hi")
    try :
        
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that agin please...")
        return "None"
    
    return query
 
if __name__ == "__main__" :
    wishMe()
    # takeCommand()
    while 1:
        # query = takeCommand().lower()
        query = input("Enter your command: ")
        # logic for executing task based on query
        if 'wikipedia' in query :
            speak("Searching Wikipedia...")
            print("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5 )
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open(sites["youtube"])
            speak(" here you go..! enjoy watching videos.")

        elif 'open instagram' in query :
            webbrowser.open(sites["instagram"])

        elif 'open google' in query:
            webbrowser.open(sites["google"])
            speak("Here is Google Home Page.")

        elif 'open stackoverflow' in query:
            webbrowser.open(sites["stackoverflow"])
            speak("Here is Stack Overflow home page.")

        elif "open github" in query :
            webbrowser.open(sites['github'])
            speak("Here is Github home page.")

        elif 'play music' in query:
            # music_dir = paths["music"]
            # songs = os.listdir(music_dir)
            music = "C:\\Users\\DELL\\Music\\Lovely Billie Eilish 320 Kbps.mp3"
            os.startfile(music)
            speak("Enjoy your music")
            break
        elif "thank u" in query :
            speak(" Welcome sir. Happy to help you.")
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, time is {strTime}")

        elif 'open vs code' in query.lower():
            os.startfile(paths['vs code']) 
            speak("Here you go..! Best of luck for your coding journey.")

        elif "Open command prompt" in query.lower():
           os.startfile(paths["cmd"])
           speak("command prompt opened successfully")

        elif "open notepad" in query.lower() :
            npp = paths["notepad"]
            os.startfile(npp)
            speak("Notepad has been opened")

        # elif "open claculator" in query.lower() :
        #     calc = paths["calc"]
        #     os.startfile(calc)
        #     speak("Here is your calculator")

        elif "open codechef" in query.lower():
            cc = sites["codechef"]
            os.startfile(cc)
            speak("Here is codechef homepage.")

        # else:
        #     speak("Bye..! See you soon.")
        #     exit()
        
        
