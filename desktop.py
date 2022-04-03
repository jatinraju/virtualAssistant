import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import ctypes
import pyjokes
import shutil
import smtplib
import subprocess
from requests import get
import winshell
import operator
import cv2
from clint.textui import progress
import pywhatkit as kit
import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import sys
import time
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[1].id)
#print(voices)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING:")
        speak("I am Star")

    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON:")
        speak("I am Star")

    else:
        speak("GOOD EVENING:")
        speak("I am Star")

def usrname():


    speak("What should i call you ")
    uname = takecommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you,")


def takecommand():#it takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')

        print(f"user said:{query}\n")
    except Exception as e:
       # printf(e)
        print("say that again please...")
        return"none"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmal.com',587)
    server.ehlo()
    server.starttls()
    server.login('bhupinderkaursukh@gmail.com','sukh4')
    server.sendmail('bhupinderkaursukh@gmail.com',to,content)
    server.close()

def TaskExecution():
    #usrname()
    #takecommand()
     wishMe()
     usrname()

     while True:
        query = takecommand().lower()  # logic for executing the tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query or "play song" in query:
            music_dir = 'C:\\Users\\lenovo\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[5]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)
        elif 'how are you' in query :
            speak("I am fine,Thank you")
            print("I am fine,Thank you")

            speak("what about you, mam")
            print("what about you, mam")

        elif 'fine' in query:
            speak("It's good to know that u r fine")
            print("It's good to know that u r fine")
        elif "thank you"in query or "thanks" in query:
            speak("it's my pleasure mam.")
        elif "you can sleep "in query or "sleep now" in query:
            speak("okay mam, i am going to sleep you can call me  anytime.")
            print("okay mam, i am going to sleep you can call me  anytime.")
            break;
            speak(pyjokes.get_joke())
        elif 'exit' in query:

        elif 'joke' in query:
            speak("Thanks for giving me your time")

        elif "who i am" in query:
            speak("If you talk then definatelLy your human.")
            print("If you talk then definatelLy your human.")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Bhupinder kaur from cse6th.")
            print("I have been created by Bhupinder kaur from cse6th.")
        elif "why you came to world" in query:

            speak("Thanks to bhupinder. further It's a secret")
            print("Thanks to bhupinder. further It's a secret")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = 'C:\\Users\\lenovo\\OneDrive\\Desktop\\project(ppt)(report)'
            os.startfile(power)

        elif 'news' in query:

            try:
                main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=83263a48521a48a797182dbc3926e513'
                main_page = requests.get(main_url).json()
                # print(main_page)
                articles = main_page["articles"]
                # print(articles)
                head = []
                day = ["first", "second", "third", "fourth", "fifth,""sixth", "seventh", "eighth", "ninth", "tenth"]
                for ar in articles:
                    head.append(ar["title"])
                for i in range(len(day)):
                    speak(f"today's{day[i]} news is:{head[i]}")
                    print(f"today's{day[i]} news is:{head[i]}")

            except Exception as e:

                print(str(e))
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

       # elif "camera" in query or "take a photo" in query:
        #    ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)
        elif "star" in query:

            wishMe()
            speak("star 1 point o in your service Mister")
            speak("listener")



        elif "do some calculations"in query or "can you calculate" in query or "can you calculate" in query:
            try:
                r=sr.Recognizer()
                with sr.Microphone() as source:
                   speak("say what you want to calculate, example :3 plus 2")
                   print("listening....")
                   r.adjust_for_ambient_noise(source)
                   audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                    '+': operator.add,#plus
                    '-': operator.sub,#minus
                    '*': operator.mul,#multiply
                    'divided':operator.__truediv__,#divided
                }[op]
                def eval_binary_expr(op1,oper,op2):#5+8
                   op1,op2=int(op1),int(op2)
                   return get_operator_fn(oper)(op1,op2)
                speak("your result is")
                print("your result is")
                speak(eval_binary_expr(*(my_string.split())))
                print(eval_binary_expr(*(my_string.split())))


            except Exception as e:
                print("none")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
        elif "send a message" in query:
            kit.sendwhatmsg("+918427383448"," helo manjot mai aeh message star to kita",9,22)
        elif " email to manjot" in query:
            try:
                speak("what should i say?")
                print("what should i say?")
                content =takecommand()
                to="manjotchohan00@gmail.com"
                sendEmail(to,content)
                speak("mail has been sent to manjot")
            except Exception as e:
                print(e)
                speak("sorry , i am not able to send this mail  to manjot")
        elif "temperature in hoshiarpur" in query:
            search = "temperature in hoshiarpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
            print(f"current{search} is {temp}")
        elif "temperature in chandigarh" in query:
            search = "temperature in chandigarh"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
            print(f"current{search} is {temp}")
        elif "temperature in delhi" in query:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")
        else:
            webbrowser.open(query)



if __name__ == "__main__":
    #wishMe()
    while True:
        permission = takecommand()
        if"wake up" in permission:
            TaskExecution()
        elif "goodbye" in permission:
            speak("thanks for using me sir,have a good day")
            sys.exit()






