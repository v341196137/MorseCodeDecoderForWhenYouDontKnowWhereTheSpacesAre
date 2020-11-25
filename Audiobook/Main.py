import pyttsx3

voice = pyttsx3.init()
with open("./Audiobook/file.txt", "r") as file:
    for line in file:
        voice.say(line)
        voice.runAndWait()