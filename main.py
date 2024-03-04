import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os
import webbrowser
import sys
import wikipedia
import operator
import datetime

    # engine = pyttsx3.init('sapi5')
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)
    # engine.setProperty('rate', 150)
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
            kit.playonyt(f"{qrry}")
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
            music_dir = 'E:\Musics'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'play iron man movie' in query:
            npath = "E:\ironman.mkv"
            os.startfile(npath)
        elif 'close movie' in query:
            os.system("taskkill /f /im vlc.exe")
        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "Lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        # elif "open notepad" in query:
            # npath = "C:\WINDOWS\system32\\notepad.exe"
            # os.startfile(npath)
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
            cv2.destroyAllWndows()
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


            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator.__truediv__,
                }[op]


            def eval_bianary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
            # elif "what is my ip address" in query:
            #         speak("Checking")
            #     try:
            #         ipAdd = requests.get('https://api.ipify.org').text
            #     print(ipAdd)
            #     speak("your ip adress is")
            #     speak(ipAdd)
            #     except Exception as e:
            #     speak("network is weak, please try again some time later")
            #     elif "volume up" in query:
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #         pyautogui.press("volumeup")
            #     elif "volume down" in query:
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #         pyautogui.press("volumedown")
            #     elif "mute" in query:
            #         pyautogui.press("volumemute")
            #     elif "refresh" in query:
            #         pyautogui.moveTo(1551,551, 2)
            #         pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            #         pyautogui.moveTo(1620,667, 1)
            #         pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

# def perform_action(query):
#     if 'open chrome' in query:
#         webbrowser.open("C:\Program Files\Google\Chrome\Application\chrome.exe")
#     elif 'close chrome' in query:
#         os.system("taskkill /f /im chrome.exe")
#     elif 'youtube search' in query:
#         query = query.replace("youtube search", "")
#         pyautogui.hotkey('alt', 'd')
#         time.sleep(1)
#         pyautogui.press('tab')
#         pyautogui.press('tab')
#         pyautogui.press('tab')
#         pyautogui.press('tab')
#         time.sleep(1)
#         pyautogui.write(f"{query}", 0.1)
#         pyautogui.press('enter')
#     elif 'open new window' in query:
#         pyautogui.hotkey('ctrl', 'n')
#     elif 'open incognito window' in query:
#         pyautogui.hotkey('ctrl', 'shift', 'n')
#     elif 'minimise this window' in query:
#         pyautogui.hotkey('alt', 'space')
#         time.sleep(1)
#         pyautogui.press('n')
#     elif 'open history' in query:
#         pyautogui.hotkey('ctrl', 'h')
#     elif 'open downloads' in query:
#         pyautogui.hotkey('ctrl', 'j')
#     elif 'previous tab' in query:
#         pyautogui.hotkey('ctrl', 'shift', 'tab')
#     elif 'next tab' in query:
#         pyautogui.hotkey('ctrl', 'tab')
#     elif 'close tab' in query:
#         pyautogui.hotkey('ctrl', 'w')
#     elif 'close window' in query:
#         pyautogui.hotkey('ctrl', 'shift', 'w')
#     elif 'clear browsing history' in query:
#         pyautogui.hotkey('ctrl', 'shift', 'delete')
#
# if __name__ == "__main__":
#     while True:
#         query = take_command().lower()
#         perform_action(query)