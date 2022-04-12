
# Chatbot
AI Based Chatbot  Made on Python Completely Opensource

#### Requirements
    Python = 3.x.x
    Pyttsx3
    speech_recognition
    pip

#### Installation

1. Clone and navigate to chatbot directory.
    ```bash
    git clone https://github.com/Neeraj-x0/Chatbot
    cd Chatbot
    ```

2. Install the required packages.
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Bot.
    ```bash
    python main.py
    ```
4. You're done and let's voicechat with your bot via Commandline.


### Using Pre-Built Modules for Your Project

- #### Text-to-Speech 
```python

from tts import * # You can Import Only 1 voice type if you want "talkm" for male voice and "talkf" for female
while True:
    talkf('This will give an output in female sound')
    talkm('This will give an output in male sound')
    break


```

- #### AI Response 
```python
from chatbot import bot

text = "Hello , How are you ?"
print(bot(text)) #This will print the response from AI

print(bot("HI")) #This will print the response from AI
```

### Author

[Neeraj](https://github.com/Neeraj-x0)

### Thanks To:
- [Natesh Bhat](https://github.com/nateshmbhat) For Pyttsx3
- [Brainshop Ai](brainshop.ai) For AI Response
