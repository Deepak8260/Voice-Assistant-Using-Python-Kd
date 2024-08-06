import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening ....')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('recognizing voice...')
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print('Not Understanding')
            
#sptext()
    

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()
    
#speechtx('Hello, Welcome to the World of A-I')

if __name__ == '__main__':
    
    
    #if sptext().lower() == "hey jarvis" :
        data1 = sptext().lower()
        if 'your name' in data1:
            name = 'My Name is jarvis'
            speechtx(name)
    
    #else:
    #    print('Thanks')
        
        
        
        
        
        
        