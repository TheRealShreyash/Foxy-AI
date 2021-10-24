import speech_recognition as sr
import pyttsx3 as pyt
import pyaudio
import pywhatkit as wht
import datetime
import wikipedia
import subprocess

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
            if 'alpha' in command:
                command = command.replace('alpha', '')
                print(command)
    except:
        pass
    return command


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

    elif 'who is technoblade' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 10)
        print(info)
        talk(info)

    elif 'do you had your breakfast' in command:
        talk('Sorry I am a machine so I cannot eat anything')

    elif 'open brave' in command:
        subprocess.call('C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe')
        talk('Opening Brave')

    elif 'open vs code' in command:
        subprocess.call('C://Users//HP//AppData//Local//Programs//Microsoft VS Code//code.exe')
        talk('Opening Vs Code')

    elif 'open world' in command:
        subprocess.call('C://Program Files//Microsoft Office//root//Office16//WINWORD.EXE')
        talk("Opening Word")

    elif 'open chrome' in command:
        subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')
        talk("Opening chrome")

    else:
        print('**********YOU DIDN\'T MENTIONED FOXY PLEASE TRY AGAIN**********')


while True:
    run_foxy()
