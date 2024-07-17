import pyttsx3
import datetime
import webbrowser
from time import sleep

engine = pyttsx3.init()

def get_command():
    command = input("You: ")
    return command.lower()

def open_website(site):
    webbrowser.open(site)

def process_command(command):
    if 'time' in command:
        hour = datetime.datetime.hour
        print(hour)
        return f"The current time is 6 PM"
    elif 'date' in command:
        return "Today's date is July 13, 2024"
    elif 'your name' in command:
        return "I am your assistant, how can I help you?"
    elif 'exit' in command:
        return "Goodbye!"
    elif 'youtube' in command or 'google' in command or 'wikipedia' in command:
        open_website(command)
        return 'opening'
    else:
        return "Sorry, I don't understand that command."

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        command = get_command()
        if command:
            response = process_command(command)
            speak(response)
            if 'exit' in command:
                break

if __name__ == "__main__":
    main()
