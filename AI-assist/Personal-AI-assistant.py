import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess as sp
from ecapture import ecapture as ec
import wolframalpha
import json 
import requests
import pyaudio
import subprocess
import tkinter 
import random 
import operator 
import winshell 
import pyjokes 
import feedparser 
import smtplib
import ctypes
import shutil
from twilio.rest  import Client
from clint.textui import progress
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning sir")
        print("Hello,Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon sir")
        print("Hello,Good Afternoon sir")
    else:
        speak("Hello,Good Evening sir")
        print("Hello,Good Evening sir")


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("##########".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("##########".center(columns))
    speak("How can i Help you, Sir")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        statement=r.recognize_google(audio,language='en-in')
        print(f"user said:{statement}\n")
    except Exception as e:
        speak("Sorry?, please say that again")
        return "None"
    return statement

if __name__=='__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()
    while True:
        statement = takeCommand().lower()

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Your personal AI assistant has stopped, Good bye')
            print('Your personal AI assistant has stopped, Good bye')
            break

        if 'wikipedia' in statement:
            speak('Yes, I am Searching Wikipedia...')
            statement =statement.replace("show wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now, here you can search any songs or movies")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now, now you can search anything..")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now, you can check all inboxes")
            time.sleep(5)

        elif "open stackoverflow" in statement:
            speak("Stack Over flow is open now. Happy coding")
            webbrowser.open("stackoverflow.com")  
 
        elif "play music" in statement or "play song" in statement:
            speak("Here you go with music. You can listen this song")
            music_dir=(r"C:\Users\Pratik\Music")
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[0]))

        elif "give me the weather update" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Please tell me the name of your city")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" Sorry, City Not Found ")

        elif "open calculator" in statement:
            sp.Popen("C:\\Windows\\System32\\calc.exe")
            speak("Calculator is opened now. You can calculate anything")

        elif 'what is the time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your persoanl assistant. I have done minor tasks like'
                  'opening youtube, google chrome, gmail, facebook, calculator, commmand prompt, predict time, take a photo, play music, search wikipedia, predict weather' 
                  'in different cities , get top headline news from times of india, even you can ask me anything and I will try to answer as much as possible!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was made by Pratik Sen")
            print("I was made by Pratik Sen")

        elif "who is pratik" in statement:
            speak("Pratik Sen is a quite good programmer with having a good knowledge of Python programming, java, React Js, Node js, Mongo DB and full stack development. Pratik has six thousand upvotes and one million views on leetcode. He is currently pursuing Btech degree in computer Science.")
            print("Pratik Sen is a quite good programmer with having a good knowledge of Python programming, java, React Js, Node js, Mongo DB and full stack development. Pratik has six thousand upvotes and one million views on leetcode. He is currently pursuing Btech degree in computer Science.")

        elif 'what is the news' in statement:
            news = webbrowser.open_new_tab("https://bartamanpatrika.com/home")
            speak('Here are some headlines from bortoman potrika, Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
 
        elif "restart" in statement:
            subprocess.call(["shutdown", "/r"])

        elif "open notepad" in statement:
            os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
            speak("notepad is opened now. You can note or write anything")

        elif "open command prompt" in statement:
            os.system('start cmd')
            speak("command prompt is opened now")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "shut down the computer" in statement:
            speak("Ok , your computer will shut down in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)