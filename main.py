import subprocess

import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os
import pydub
import webbrowser
import sys
import wikipedia
import operator
import datetime
import cv2

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Ready To Comply. What can I do for you ?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r= r.adjust_for_ambient_noise()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        elif "search on youtube" in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            # kit.playonyt(f"{qrry}")
            webbrowser.open(f"{qrry}")
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")
        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)
        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")
        elif 'play music' in query:
            subprocess.call("spotify.exe")
            # def play_audio(file_path):
            #    pygame.mixer.init()
            #    pygame.mixer.music.load("C:\Users\BAALA GURU\Music\A52s5G")
            #    pygame.mixer.music.play()
            #    play_audio('audio_file.mp3')
               # music_dir = '../../Music/A52s5G'
            # songs = os.listdir(music_dir)
            # os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "shut down " in query:
            os.startfile("shutdown.bat")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "Lock" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "open notepad" in query:
            os.startfile("C://WINDOWS//system32//notepad.exe")
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "go to sleep" in query:
            speak(' alright then, I am switching off')
            sys.exit()
        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listning...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
        elif "search on youtube" in query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={source}")
        elif "open steam" in query:
            subprocess.call("C:\Program Files (x86)\Steam\steam.exe")
        elif "open obs studio" in query:
            os.system("../../../../ProgramData/Microsoft/Windows/Start Menu/Programs/OBS Studio/OBS Studio (64bit).lnk")
        elif "open edge" in query:
            subprocess.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        elif "command prompt" in query:
            subprocess.call("cmd.exe")
        elif "open chrome" in query:
            subprocess.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
        elif "open bleach" in query:
            subprocess.call("BLEACH Brave Souls - 3D Action.exe")
        elif "open pc manager" in query:
            subprocess.call("C:\Program Files\Microsoft PC Manager\MSPCManager.exe")
        elif "open power toys" in query:
            subprocess.call("C:\Program Files\PowerToys\PowerToys.exe")
        elif "open voice" in query:
            subprocess.call("C:\Program Files\Voice.ai\VoiceAI.exe")
        elif "let's play" in query:
            os.startfile("C://Users//BAALA GURU//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Steam//BLEACH Brave Souls - 3D Action.url")
