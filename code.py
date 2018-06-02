import speech_recognition as sr
import pyaudio
from googlesearch import search
import webbrowser
from gtts import gTTS
from playsound import playsound
#MAIN CONTENT BODY
index = pyaudio.PyAudio().get_device_count() - 1
#Selecting language
language_selection="Select Language"
lanobj=gTTS(text=language_selection,lang='en',slow=False)
lanobj.save("languageselect.mp3")
playsound('languageselect.mp3')
t=sr.Recognizer()
with sr.Microphone() as source:
    audio=t.listen(source)
try:
    print("Task completed")
    lselected="Language selected by you is " + t.recognize_google(audio)
    if t.recognize_google(audio)=='Hindi':
        print("Hindi")
        language='hi'
    elif t.recognize_google(audio)=='English':
        print("English")
        language='en'
    laselected=gTTS(text=lselected,lang='en',slow=False)
    laselected.save("langselected.mp3")
    playsound('langselected.mp3')
except sr.UnknownValueError:
    langerror = "Google did not understand you"
    langerroro = gTTS(text=langerror, lang=language, slow=False)
    langerroro.save("error0.mp3")
    playsound('error0.mp3')
voice="Say something"
fobj=gTTS(text=voice,lang=language,slow=False)
fobj.save("say.mp3")
playsound('say.mp3')
r=sr.Recognizer()
with sr.Microphone() as source:

    audio=r.listen(source)
try:
    print("Task completed")
    svoice="Google Speech Recognition think you said"+r.recognize_google(audio)
    sobj=gTTS(text=svoice,lang='en',slow=False)
    sobj.save("repeat.mp3")
    playsound('repeat.mp3')
except sr.UnknownValueError:
    thirdvoice = "Google did not understand you"
    thirdobj = gTTS(text=thirdvoice, lang='en', slow=False)
    thirdobj.save("error.mp3")
    playsound('error.mp3')
except sr.RequestError as e:
    print("Request error done:{0}".format(e))


query = r.recognize_google(audio)
#for j in search(query, tld="com", num=1, stop=1, pause=2):
    #   print(j)
    #  webbrowser.open(j)
import wikipedia
result=wikipedia.summary(query,sentences=3)
print("Task completed")
languages=language
myobj=gTTS(text=result,lang=languages,slow=False)
myobj.save("wiki.mp3")
playsound('wiki.mp3')