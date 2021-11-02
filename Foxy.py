# THESE IMPORTS ARE REQUIRED FOR THIS AI TO RUN

import speech_recognition as sr
import pyttsx3 as pyt
import pyaudio
import pywhatkit as wht
import datetime
import wikipedia
import subprocess
import webbrowser
import smtplib

# Making a new listener
listener = sr.Recognizer()

#  making an engine that will speak to the user
engine = pyt.init()

# changing the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


# making engine talk
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'foxy' in command:
                command = command.replace('foxy', '')
                print(command)
    except:
        pass
    return command

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def run_foxy():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        wht.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I: %M %p')
        print(time)
        talk("Current time is" + time)

    elif 'do you had your breakfast' in command:
        talk('Sorry I am a machine so I cannot eat anything')

    elif 'you are bad' in command:
        talk('Common nerd i am not your father\'s servant')

    elif 'about' in command:
        talk('I am currently under development I am in Version 1 now!')

    elif 'open gx' in command:
        subprocess.call('C://Users//HP//AppData//Local//Programs//Opera GX//launcher.exe')
        talk('Opening GX')

    elif 'open vs code' in command:
        subprocess.call('C://Users//HP//AppData//Local//Programs//Microsoft VS Code//code.exe')
        talk('Opening Vs Code')

    elif 'open world' in command:
        subprocess.call('C://Program Files//Microsoft Office//root//Office16//WINWORD.EXE')
        talk("Opening Word")

    elif 'open chrome' in command:
        subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')
        talk("Opening chrome")

    elif 'open Intellij' in command:
        subprocess.call('E://IntelliJ IDEA Community Edition 2021.2.1//bin//idea64.exe')
        talk("Opening Intellij")

    elif 'open pychram' in command:
        subprocess.call('E://PyCharm Community Edition 2021.2.2//bin//pyharm64.exe')
        talk("Opening Pycharm")

    elif 'open youtube' in command:
            webbrowser.open("www.youtube.com")
            talk("Opening Youtube")

    elif 'open twitter' in command:
            webbrowser.open("www.twitter.com")
            talk("Opening Twitter")

    elif 'open twitch' in command:
            webbrowser.open("www.twitch.tv")
            talk("Opening Twitch")

    elif 'open github' in command:
            webbrowser.open("www.github.com")
            talk("Opening Github")

    elif 'open amazon' in command:
            webbrowser.open("www.amazon.com")
            talk("Opening Amazon")

    elif 'open name mc' in command:
            webbrowser.open("www.namemc.com")
            talk("Opening Namemc")

    elif 'email to xyz' in command:
            try:
                talk("What should I say?")
                content = take_command()
                to = "xyz@gmail.com"    
                sendEmail(to, content)
                talk("Email has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry my friend. I am not able to send this email")    


    else:
        print('**********YOU DIDN\'T MENTIONED FOXY PLEASE TRY AGAIN**********')
        talk('Please Read Console and say the command again')


while True:
    run_foxy()