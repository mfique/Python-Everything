import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import wolframalpha
# import distutils

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0 - male, 1 - female
activationWord = 'computer'

def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

        try:
            print('Recognizing speech ...')
            query = listener.recognize_google(input_speech, language='en_gb')
            print(f'The input speech was: {query}')
            return query.lower()
        except Exception as exception:
            print('I did not quite catch that')
            speak('I did not quite catch that')
            print(exception)
            return 'None'

# Main loop
if __name__ == '__main__':
    speak('All systems nominal')

    while True:
        # Parse a list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            # List commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings, all.')
                else:
                    query.pop(0)  # remove 'say'
                    speech = ' '.join(query)
                    speak(speech)
