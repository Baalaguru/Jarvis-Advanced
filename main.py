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
    user_name = "Gru"
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(f"Good Morning! {user_name}")
        speak(f"Good Morning! {user_name}")
    elif hour >= 12 and hour < 18:
        print(f"Good Afternoon! {user_name}")
        speak(f"Good Afternoon! {user_name}")

    else:
        print(f"Good Evening! {user_name}")
        speak(f"Good Evening! {user_name}")

    speak(f"Ready To Assist you. What can I do for you {user_name}?")

print("network is not responding....")
speak("network is not responding....")
def takeCommand():


    if False :
        r = sr.Recognizer()
        with (sr.Microphone() as source):
            r= r.adjust_for_ambient_noise(source)
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
    else:


        query = input("Enter your query : ")
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("what should I search ?")
            query = takeCommand().lower()
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            print("Openning outube")
            webbrowser.open("https://www.youtube.com/")
        elif "search on youtube" in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            webbrowser.open(f"www.youtube.com/results?search_query={qrry}")
        elif "search on youtube" in query:
            os.system("taskkill /f /im chrome.exe")
        elif "close youtube" in query:
            os.system("taskkill /f /im msedge.exe")
        elif "open google" in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)
        elif "close edge" in query:
            os.system("taskkill /f /im msedge.exe")
        elif "play music" in query:
            subprocess.call("spotify.exe")
        elif "help" in query:
            cmds = ["wikipedia","open youtube","search on youtube","close youtube","open google","close edge","play music","time","shutdown","restart the system",
                    "check for updates","lock system","open notepad","close notepad","open command prompt","close command prompt","open camera","go to sleep",
                    "take screenshot","open steam","open obs studio","open pc manager","open power toys","open voice","let's play","shutdown pc","help"]
            print("commands list....")
            for i in  cmds:
                print(f"{i}")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "shutdown" in query:
            os.startfile("C://Users//BAALA GURU//PycharmProjects//Jarvis//SlideToShutDown.lnk")
        elif "restart the system" in query:
            os.startfile("C://Users//BAALA GURU//PycharmProjects//Jarvis//restart_pc.bat")
        elif "check for updates" in query:
            os.startfile("C://Users//BAALA GURU//PycharmProjects//Jarvis//check_windows_update.cmd")
        elif "lock system" in query:
            os.startfile("C://Users//BAALA GURU//PycharmProjects//Jarvis//lock_pc.bat")
        elif "open notepad" in query:
            os.startfile("C://WINDOWS//system32//notepad.exe")
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
        elif "open command prompt" in query:
            speak("openning Command Prompt....")
            print("openning Command Prompt....")
            os.system("start cmd")
        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")
        elif "open camera" in query:
            pass
        #     os.system("C://Windows//System32//camera.exe")

            # cap = cv2.VideoCapture(VideoCapture0)
            # while True:
            #     ret, img = cap.read()
            #     cv2.imshow('webcam', img)
            #     k = cv2.waitKey(50)
            #     if k == 27:
            #         break;
            # cap.release()
            # cv2.destroyAllWindows()
        elif "go to sleep" in query:
            print(' alright then, I am switching off')
            speak(' alright then, I am switching off')
            sys.exit()
        elif "take screenshot" in query:
            speak("tell me a name for the file")
            print("tell me a name for the file")
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")
            print("screenshot saved")
        elif "search on youtube" in query:
            speak("what should I search ?")
            print("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={qry}")
        elif "open steam" in query:
            speak("openning Steam....")
            print("openning Steam....")
            subprocess.call("C:\Program Files (x86)\Steam\steam.exe")
        elif "open obs studio" in query:
            speak("openning OBS Studio....")
            print("openning OBS Studio....")
            os.startfile("C://ProgramData//Microsoft//Windows//Start Menu//Programs//OBS Studio//OBS Studio (64bit ).lnk")
        elif "open vlc" in query:
            speak("Openning VLC media player ....")
            print("Openning VLC media player ....")
            os.startfile("C://ProgramData//Microsoft//Windows//Start Menu//Programs//VideoLAN//VLC media player.lnk")
        elif "open edge" in query:
            speak("openning Microsoft Edge....")
            print("openning Microsoft Edge....")
            subprocess.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        elif "open chrome" in query:
            speak("openning Chrome....")
            print("openning Chrome....")
            subprocess.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
        elif "open pc manager"  in query:
            subprocess.call("C:\Program Files\Microsoft PC Manager\MSPCManager.exe")
        elif "open power toys" in query:
            subprocess.call("C:\Program Files\PowerToys\PowerToys.exe")
        elif "open voice" in query:
            subprocess.call("C:\Program Files\Voice.ai\VoiceAI.exe")
        elif "let's play" in query:
            os.startfile("C://Users//BAALA GURU//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Steam//BLEACH Brave Souls - 3D Action.url")
        elif "shutdown pc" in query:
            subprocess.run([r"C:\Users\BAALA GURU\PycharmProjects\Jarvis\SlideToShutDown.lnk"])
