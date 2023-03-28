import speech_recognition as sr
import pyttsx3

recog = sr.Recognizer()

def SpeakText(command):
    out = pyttsx3.init()
    if (command != 'desligar'):
        out.say(command)
    else:
        out.say('Ok! Estou desligando...')
    out.runAndWait()

text = ''

while(text != 'desligar'):
    try:
        with sr.Microphone() as mic:
            recog.adjust_for_ambient_noise(mic)
            print("AI: Listening...")
            audio = recog.listen(mic)
            text = recog.recognize_google(audio, language='en-US')
            text = text.lower()
            print("IA: You say '" + text + "'")
            SpeakText(text)
    
    except sr.RequestError as e:
        print('Error: Unable to execute the request; {0}'.format(e))

    except sr.UnknownValueError:
        print('Error: An unknown error has occurred!')