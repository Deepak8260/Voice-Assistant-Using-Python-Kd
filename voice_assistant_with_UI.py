import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime as dt
import tkinter as tk
from tkinter import font
from tkinter import scrolledtext
import threading

assistant_active = False

# Initialize the text-to-speech engine
def speechtx(x):
    engine = pyttsx3.init()
    voice_list = engine.getProperty('voices')#This retrieves a list of available voice objects from the engine.
    engine.setProperty('voice', voice_list[0].id)#This sets the voice property of the engine using the id of the first voice in the list. The id is a unique string identifier for the voice. 
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

# Function to handle speech recognition and command processing
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        append_to_text_area('\nListening ....')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            append_to_text_area('Recognizing voice...')
            data = recognizer.recognize_google(audio)
            append_to_text_area(f'Recognized: {data}')
            process_command(data.lower())
        except sr.UnknownValueError:
            append_to_text_area('Command not recognised. Try Once more')

# Process the recognized command
def process_command(data1):
        global assistant_active
        if 'wake up jarvis' in data1 or 'wake up' in data1 or 'wake' in data1 or 'hey jarvis' in data1:
            # Activate the assistant
            assistant_active = True
            response = "Hi sir, I am Jarvis, your personal voice assistant. How may I help you sir?"
            speechtx(response)
            append_to_text_area(response)
            
        elif not assistant_active:
            # If the assistant is not active, ignore all other commands
            append_to_text_area("Please say the desired command to activate Jarvis.")
            return
        if 'your name' in data1:
            name = 'My Name is Jarvis'
            speechtx(name)
            append_to_text_area(name)
            
        elif 'old are you' in data1 or 'your age' in data1 or 'you born' in data1:
            age = 'I have been created on 6th August 2024 at 12:40 AM. I hope this data helps you to find my age.'
            speechtx(age)
            append_to_text_area(age)
            
        if 'thanks' in data1 or 'thank you' in data1 or 'thank you jarvis' in data1 :
            answer = "Most welcome sir ! It's my pleasure . What more I can help you with ?"
            speechtx(answer)
            append_to_text_area(answer)
            
        elif 'time' in data1:
            time = "It's " + dt.datetime.now().strftime('%I:%M %p')
            speechtx(time)
            append_to_text_area(time)
            
        elif 'youtube' in data1:
            webbrowser.open('https://www.youtube.com/')
            append_to_text_area("Opening YouTube...")
            
        elif 'google' in data1:
            webbrowser.open('https://www.google.com/')
            append_to_text_area("Opening Google...")
            
        elif 'linkedin' in data1:
            webbrowser.open('https://www.linkedin.com/')
            append_to_text_area("Opening LinkedIn...")
            
        elif 'my name' in data1:
            myName = "Yes , You are the host and your name is Kumar Deepak"
            speechtx(myName)
            append_to_text_area(myName)
            
        elif 'friends' in data1:
            myFriends = "Yes , you have total 5 friends. They are Chandrakanta, Ricky , Rachana, Archana and Tarun"
            speechtx(myFriends)
            append_to_text_area(myFriends)
            
            
        elif 'exit' in data1:
            speechtx("Thank You Boss")
            append_to_text_area("Exiting...")
            root.quit()
    

# Function to append text to the text area
def append_to_text_area(text):
    text_area.insert(tk.END, text + '\n')
    text_area.yview(tk.END)
    root.update()

# Function to start speech recognition in a new thread
def start_listening():
    threading.Thread(target=sptext, daemon=True).start()


# Tkinter UI setup
root = tk.Tk()
root.title("Jarvis Voice Assistant")

# Create a Font object with the desired size
my_font = font.Font(family="Helvetica", size=16)  # Change the size as needed

# Create a text area for displaying messages
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=60,font=my_font)
text_area.pack(padx=10, pady=10)

# Create a button to start listening
listen_button = tk.Button(root, text="Listen", command=start_listening)
listen_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
