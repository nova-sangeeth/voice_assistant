import speech_recognition as sr
from time import ctime
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            # print(voice_data)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry speech is down')
        return voice_data

# Change all the print statements to the print method.
def nova_speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

 
def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My name is Nova')
    if 'what time is it ' in voice_data:
        # print(f'the time is {ctime()}')
        print(ctime)
    if 'search' in voice_data:
        search = record_audio('What do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here are the results' + search)
# find the correct url
    if 'find location' in voice_data:
        location = record_audio('say your location....')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('The location is' + location)
    # if 'weather' in voice_data:
    #     weather = record_audio('Tell me your location.')
    #     url = 'https://www.accuweather.com/en/browse-locations' + location 
    #     webbrowser.get().open(url)
        print('Here are the results')
    if 'exit' in voice_data:
        exit()


time.sleep(1)
print('Say something')
while 1:
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)