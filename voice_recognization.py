# Before going to do this you must install
# sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio
# pip install PyAudio
# pip install SpeechRecognition

# if it not works try it
# pip install pyaudio
# pip install --upgrade pyaudio
# pip install wheel
# pip install google-api-python-client
# sudo apt-get install flac
# pip install monotonic
# pip install SpeechRecognition


import speech_recognition as sr

r = sr.Recognizer() # to recognize our audio
with sr.Microphone() as source: # to intilize our microphone
    print("Speak Anything :")
    audio = r.listen(source) # to recognizer as a source
    try:
        text = r.recognize_google(audio)    # for recognize using google this will convert text
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")