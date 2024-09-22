import speech_recognition as sr
import pyttsx3
import datetime
import os

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', id)
    print("")
    print(f"==> Asst AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def wish():
    hr = int(datetime.datetime.now().hour)

    if hr>=0 and hr<=12:
        speak("Good morning")
    elif hr>=12 and hr<=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Please tell me how can I help you")

def speechrecognition():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening for speech recognition....')
            r.pause_threshold = 1
            audio = r.listen(source,0,8)

        try:
            print('Recognizing speech recognition...')
            query = r.recognize_google(audio,language='en-in')
            print("")
            print(f"==> Captain : {query}")
            return query.lower()
        
        except:
            return "none"
        

def MainExe(query):
    Query = str(query).lower()
    if "hello" in Query:
        speak("Hello sir, welcome back")

    elif "bye" in Query:
        speak("Nice to meet you sir, Have a nice day")

    elif "good night" in Query:
        speak("Wishing you a very good night . Take care of yourself and sweet dreams")

    elif "time" in Query:
        from datetime import datetime
        time = datetime.now().strftime("%H:%M")
        speak(f"The Time Now Is : {time}")

    elif "open notepad" in Query:
        npath = "C:\\Windows\\notepad.exe"
        os.startfile(npath)

    elif "prompt" in Query:
        os.system("start cmd")

while True:
    Query = speechrecognition()
    MainExe(Query)