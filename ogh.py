import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# a speech engine initialization

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0]. id) # 0 - male, 1 - female
activationWord = 'computer' #single word

def speak(text, rate = 120):
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
            print('Recognition speech ...')
            query = listener.recognize_google(input.speech, language='en_gb')
            print(f'The input speech was: (query)')
        except Exception as exception:
            print('I did not quite catch that')
            speak('I did not quite catch that')
            print(exception)
            return 'None'
        
        return query
    
    #Main loop
if __name__== '_main_':
    speak('All system nominal')

    while True:
        #Parse a list
        query = parseCommand().lower().split()

        if query[0] == activationWord:
            query.pop(0)

            #List commands
            if query[0] == 'say':
                if 'Hello' in query:
                    speak('Greetings, all.')
                else:
                    query.pop(0) #remove say
                    speech = ''.join(query)
                    speak(speech)


