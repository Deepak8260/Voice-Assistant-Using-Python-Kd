# 🤖 JARVIS Voice Assistant

Welcome to the **JARVIS Voice Assistant** project! 🚀 This project is a simple yet powerful voice assistant built using Python. JARVIS is designed to respond to voice commands, perform a variety of tasks, and interact with users through an intuitive graphical interface created with Tkinter.

## **Level Of Project**
**Beginner**

## 📜 **Features**

- **Voice Activation**: Say "wake up Jarvis" to activate the assistant.
- **Interactive Commands**:
  - **Introduction**: Get to know JARVIS with commands like "your name" or "my name."
  - **Current Time**: Ask for the time with the "time" command.
  - **Web Navigation**: Open popular websites like YouTube, Google, and LinkedIn.
  - **Personal Information**: Learn about yourself and your friends.
- **Exit Command**: Close the application using the "exit" command.

## 🛠️ **Installation and Setup**

To get started with JARVIS, follow these steps:

1. **Install Dependencies**: Make sure you have the required libraries installed. Run the following command:

    ```bash
    pip install pyttsx3 SpeechRecognition
    ```

2. **Run the Application**: Execute the Python script to launch the JARVIS voice assistant.

## 🚀 **How to Use**

1. **Start the Application**: Run the script to start the JARVIS voice assistant.
2. **Activate JARVIS**: Click the "Listen" button or speak to begin interaction.
3. **Issue Commands**: Use the commands listed below to interact with JARVIS.
4. **Exit**: Say "exit" to close the application.

## 🗣️ **Commands**

- **🔊 Activate Assistant**:
  - `wake up jarvis`: Activates JARVIS and makes it ready to receive commands.

- **ℹ️ Get Information**:
  - `your name`: JARVIS introduces itself as "Jarvis."
  - `old are you`, `your age`, `you born`: JARVIS provides information about its creation date and time.
  - `my name`: JARVIS acknowledges your name as Kumar Deepak.
  - `friends`: JARVIS lists your friends: Chandrakanta, Ricky, Rachana, Archana, and Tarun.

- **🕒 Get Time**:
  - `time`: JARVIS provides the current time.

- **🌐 Open Websites**:
  - `youtube`: Opens YouTube in your default web browser.
  - `google`: Opens Google in your default web browser.
  - `linkedin`: Opens LinkedIn in your default web browser.

- **❌ Exit Application**:
  - `exit`: Closes the application and thanks the user.

## 🔧 **Code Overview**

Here's a brief overview of the main components:

- **Text-to-Speech Engine**: Uses `pyttsx3` to convert text into speech.

    ```python
    def speechtx(x):
        engine = pyttsx3.init()
        ...
    ```

- **Speech Recognition**: Uses `speech_recognition` to listen and process commands.

    ```python
    def sptext():
        recognizer = sr.Recognizer()
        ...
    ```

- **Command Processing**: Interprets commands and performs actions.

    ```python
    def process_command(data1):
        if 'wake up jarvis' in data1:
            ...
    ```

- **Tkinter UI**: Provides a graphical interface with a text area and a button.

    ```python
    root = tk.Tk()
    ...
    ```

## 🖼️ **Screenshots**

![JARVIS Voice Assistant](Screenshot%20(285).png)  
*Example of the JARVIS Voice Assistant interface*

## 🧑‍💻 **Contributing**

Contributions are welcome! If you have suggestions, issues, or improvements, please submit a pull request or create an issue.

## 📞 **Contact**

For any questions or inquiries, please reach out to:
- **Name**: Deepak Kumar Mohanty
- **LinkedIn**: [Visit LinkedIn Id](https://www.linkedin.com/in/deepak-kumar-mohanty-09aa59230/)
