from pyChatGPT import ChatGPT
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

#PLEASE FOLLOW THE INSTRUCTIONS TO GET YOUR ACCESS TOKEN
session_token = 'YOUR_TOKEN_HERE'
api = ChatGPT(session_token)  # auth with session token

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

# Função para ouvir e reconhecer a fala
def start_microphone(language,country,speech_language):
    # Habilita o microfone do usuário
    microphone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de reducao de ruidos no som
        microphone.adjust_for_ambient_noise(source)

        # Frase para o usuario dizer algo
        print("Listening... ")

        # Armazena o que foi dito numa variavel
        audio = microphone.listen(source)

    try:

        # Passa a variável para o algoritmo reconhecedor de padroes
        speech = microphone.recognize_google(audio, language=speech_language)

        # Retorna a frase pronunciada
        print("You said: " + speech)
        resp = api.send_message(speech)
        print('\n'+resp['message']+'\n')
        give_voice(resp['message'],language,country)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Didn't understand.")

    return speech

print('The default language is brazilian PORTUGUESE. If you want to change for english, please press L\l.\n')
language = 'pt'
country = 'com.br'
speech_language = 'pt-BR'
while True:
    print('L\l to change for english.\n\n')
    key = input('When you be ready to talk with ChatGPT, please press ENTER.')
    if key == 'L' or key=='l':
        language = 'en'
        country = 'us'
        speech_language ='en-US'
    start_microphone(language,country,speech_language)
    os.system("clear")
