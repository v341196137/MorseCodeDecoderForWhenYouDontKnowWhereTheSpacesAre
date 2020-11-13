import pyttsx3

voice = pyttsx3.init()
file = open("./Audiobook/file.txt", "r")
for line in file:
    voice.say(line)
    voice.runAndWait()