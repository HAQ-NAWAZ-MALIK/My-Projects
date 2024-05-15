import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)

# Function to speak the given text
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen for and recognize speech commands
def get_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            print(command)
    except:
        pass
    return command

# Main function to handle commands
def run_assistant():
    command = get_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + current_time)

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)

    elif 'date' in command:
        speak('sorry, I have a headache')

    elif 'are you single' in command:
        speak('I am in a relationship with wifi')

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    else:
        speak('Please say the command again.')

# Run the assistant in a loop
while True:
    run_assistant()
