import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#if  name  == " main ":
# def usrname():
speak("hello sir")