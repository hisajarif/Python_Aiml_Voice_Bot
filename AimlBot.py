
# coding: utf-8

# In[ ]:


import time
import speech_recognition as sr
import wikipedia
import pyttsx3
import os
import aiml


# In[ ]:


def speaks(audioString):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.say(audioString)
    engine.runAndWait()
    
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data


# In[ ]:


def jarvis(data):
    if "hi" in data:
        speaks("hi, how do you do")
 
    elif "what time is it" in data:
        speaks(ctime())

    else if "who made you" in data:
        speaks("I am an technology developed by you ")
        
    elif "who is" in data:
        data = data.replace('who is ','')
        speaks(wikipedia.summary(data))
        
    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speaks("Hold on, I will show you where " + location + " is.")
        os.system("start chrome https://www.google.nl/maps/place/" + location + "/&amp;")
    else:
        s = kernel.respond(data)
        speaks(s)


# In[ ]:


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml")
    kernel.saveBrain("bot_brain.brn")
 
# initialization
time.sleep(2)
speaks("Hi, what can I do for you?")
#while True:
for i in range(3):
    data = recordAudio()
    jarvis(data)
    

