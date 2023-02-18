import speech_recognition as sr


# Função para ouvir e reconhecer a fala
def start_microphone():
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
        speech = microphone.recognize_google(audio, language='pt-BR')

        # Retorna a frase pronunciada
        print("You said: " + speech)

    # Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Didn't understand.")

    return speech