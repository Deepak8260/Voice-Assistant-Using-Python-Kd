import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime as dt


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening ....')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('Recognizing voice...')
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print('Not Understanding')
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    while True:
        data1 = sptext().lower()
        
        if 'your name' in data1:
            name = 'My Name is Jarvis'
            speechtx(name)
            
        elif 'old are you' in data1 or 'your age' in data1 or 'you born' in data1:
            age = 'I have been created on 6th August 2024 at 12:40 AM. I hope this data helps you to find my age.'
            speechtx(age)
            
        elif 'time' in data1:
            time = "Ya sure! It's " + dt.datetime.now().strftime('%I:%M %p')
            speechtx(time)
            
        elif 'youtube' in data1:
            webbrowser.open('https://www.youtube.com/')
            
        elif 'exit' in data1:
            speechtx("Thank You Boss")
            break
    
    