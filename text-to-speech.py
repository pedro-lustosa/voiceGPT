# Import the required module for text
# to speech conversion
from gtts import gTTS
import os
import playsound

def give_voice(text,language = 'pt',country = 'com.br'):

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    tts = gTTS(text=text, lang=language, tld=country, slow=False)
    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    return