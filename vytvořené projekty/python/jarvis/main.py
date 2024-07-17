import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime
import smtplib
from time import sleep

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Email settings (configure these with your email details)
EMAIL = "honzikpaulik2@gmail.com"
PASSWORD = "yourpassword"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return "None"

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Sorry, the service is down.")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"
    return query

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I assist you today?")

def open_website(site):
    webbrowser.open(site)

def search_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def send_email(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to, content)
        server.close()
        speak("Email has been sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
        speak("I am unable to send the email.")

if __name__ == "__main__":
    greet_user()
    while True:
        command = take_command().lower()
        print(f"command: {command}")

        if 'wikipedia' in command:
            speak("Searching Wikipedia...")
            command = command.replace("wikipedia", "")

        elif 'open youtube' in command:
            open_website("https://www.youtube.com")
            speak("YouTube is now open")

        elif 'open google' in command:
            open_website("https://www.google.com")
            speak("Google is now open")

        elif 'time' in command:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")

        elif 'send email' in command:
            try:
                speak("What should I say?")
                content = take_command()
                speak("Who should I send it to?")
                to = "recipient@example.com"  # Replace with the recipient's email
                send_email(to, content)
            except Exception as e:
                speak("Sorry, I am not able to send the email.")

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break

        sleep(1)  # Adjust sleep time as necessary
