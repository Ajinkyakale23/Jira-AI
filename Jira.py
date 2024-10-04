from http import server
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib






engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I Jeera !! code by Ajinkya . Please tell me how may i help you Sir")


def takeCommand():
    # It take microphone input form the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',534)
    server.ehlo()
    server.starttls()
    server.login("kaleajinkya2003@gmail.com", 'Ajinkyakale@23')
    server.sendmail("kaleajinkya2003@gmail.com", to,content)
    server.close()

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)


if __name__ == "__main__":
    speak("YOur are my firest")

if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir="D:\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif ' what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ajinkya' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "kaleajinkya2003@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ajinkya , I am not able to send this email")
        

if quit in query:
    exit()

