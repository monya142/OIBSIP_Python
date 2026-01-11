import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't understand.")
        return ""

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

def tell_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {date}")

def search_google(query):
    speak(f"Searching for {query}")
    webbrowser.open("https://www.google.com/search?q=" + query)


speak("Hello! I am your voice assistant")

while True:
    command = take_command()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "search" in command:
        query = command.replace("search", "")
        search_google(query)

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        break
