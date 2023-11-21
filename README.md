
# Chatbot
AI Based Chatbot  Made on Python Completely Opensource

#### Requirements
| Sl.No| Name            | Description |
|:--: | :---           |    :----   |
| 1 . | Python =< 3.x.x | Python For Running the project      |
| 2 . | Pyttsx3         | For Text-to-Speech       |
| 3 . | speech_recognition | For Speech-to-Text |
| 4 . | Pip| For installing packages|

    

 
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

## Using Your Own Customizable AI
   **Do you know that you can train your AI bot with your own details,<br>**
    **yes you can Change the url of Api Response with yours Now** <br>
    **Find the URL [HERE](https://github.com/Neeraj-x0/Chatbot/blob/main/chatbot.py#L5)** <br>
 - Read [Wiki](https://github.com/Neeraj-x0/Chatbot/wiki/How-to-get-AI-URL) to Know How to get a new URL
 
### Author

[Neeraj](https://github.com/Neeraj-x0)

### Thanks To:

- [Natesh Bhat](https://github.com/nateshmbhat) For Pyttsx3
- [Brainshop Ai](brainshop.ai) For AI Response
