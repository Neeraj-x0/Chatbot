import  pyttsx3
tts=pyttsx3.init()
voices=tts.getProperty('voices')
tts.setProperty("rate", 178)

def talkf(text):

  tts.setProperty("voice", voices[1].id)
  tts.say('<pitch middle="30">'+text+'</pitch>')
  tts.runAndWait()

def talkm(text):

  tts.setProperty("voice", voices[0].id)
  tts.say('<pitch middle="30">'+text+'</pitch>')
  tts.runAndWait()