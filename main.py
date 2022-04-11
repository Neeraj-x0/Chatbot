
from time import sleep
from urllib.request import urlopen as conn

import speech_recognition as sr
from chatbot import *
from tts import *

r= sr.Recognizer()
with sr.Microphone() as source:
    print ('Activated')
    talkm('Activated')
    talkf('Listening For input......')

    while True :

        try:
            
            
            audio = r.listen(source)
            text = r.recognize_google(audio) 
            print('User :',text) 
            if "protocol 276" in text:
                print('Enabling Protocol 276')
                talkf('Enabling Protocol 2 7 6')
                   
                break              
            else:
                print(bot(text))
                talkf(bot(text))
                
            
                
        except:
            sleep(3)    
            print('Bot : Voice Not Recognized')
            talkm('Voice Not Recognized')
    
            
      
        
              
        
