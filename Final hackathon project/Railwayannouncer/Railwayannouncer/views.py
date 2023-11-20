from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator, LANGUAGES
from indic_transliteration import sanscript
from gtts import gTTS
import os
import pyttsx3
import time
import socket
# from unidecode import unidecode


def index(request):
    return render(request,'index.html')
def searchbareng(request):
    return render(request,'searchbareng.html')
def searchbarhindi(request):
    return render(request,'searchbarhindi.html')
def searchbarmarathi(request):
    return render(request,'searchbarmarathi.html')


def anounceineng(request):
    english_text = request.GET.get('Text','default').upper()
    print(english_text)


    def is_internet_available():
        try:
            # Try to connect to a well-known website (in this case, Google's DNS server)
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False

    if is_internet_available():
        # Code to run when there is an active internet connection
        print("Internet is available. Running code which uses google api.")
        # Your code A here
        def translate_to_hindi(text):
            translator = Translator()
            translated_text = translator.translate(text, src='en', dest='hi')
            return translated_text.text

        # english_text = text
        hindi= translate_to_hindi(english_text)


        def translate_to_marathi(text):
            translator = Translator()
            translated_text = translator.translate(text, src='en', dest='mr')
            return translated_text.text

        marathi = translate_to_marathi(english_text)

        text_to_speak = english_text  # Replace with your desired text
        txt = (request.GET.get('text','default'))
        print(txt)
        tts = gTTS(text=text_to_speak, lang='en')
        tts.save('media/speecheng.mp3')
        
        text_to_speak = hindi  # Replace with your desired text
        txt = (request.GET.get('text','default'))
        print(txt)
        tts = gTTS(text=text_to_speak, lang='hi')
        tts.save('media/speechhi.mp3')
        
        text_to_speak = marathi  # Replace with your desired text
        txt = (request.GET.get('text','default'))
        print(txt)
        tts = gTTS(text=text_to_speak, lang='mr')
        tts.save('media/speechmr.mp3')

        params = {'english':english_text, 'hindi':hindi, 'marathi':marathi}
    else:
        # Code to run when there is no active internet connection
        print("No internet connection. Running code B.")
        # Your code B here




# params = {'english':text, 'hindi':hindi, 'marathi':marathi}
    return render(request,'anounce.html',params)
        










































































def anounceinhindi(request):
    text = (request.GET.get('Text','default'))
    print(text)
    def roman_to_hindi(text):
        hindi = sanscript.transliterate(text, sanscript.HK, sanscript.DEVANAGARI)
        return hindi
    romanized_text = text
    hindi_text = roman_to_hindi(romanized_text)
    
    def translate_hindi_to_english(text):
        translator = Translator()
        translated_text = translator.translate(text, src='hi', dest='en')
        return translated_text.text
    english_translation = translate_hindi_to_english(hindi_text)
    
    def translate_english_to_hindi(text):
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='hi')
        return translated_text.text
    hindi = translate_english_to_hindi(english_translation)
    
    def translate_to_marathi(text):
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='mr')
        return translated_text.text

    marathi = translate_to_marathi(english_translation)
    text_to_speak = english_translation  # Replace with your desired text
    txt = (request.GET.get('text','default'))
    print(txt)
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save('media/speecheng.mp3')
    
    text_to_speak = hindi  # Replace with your desired text
    txt = (request.GET.get('text','default'))
    print(txt)
    tts = gTTS(text=text_to_speak, lang='hi')
    tts.save('media/speechhi.mp3')
    
    text_to_speak = marathi  # Replace with your desired text
    txt = (request.GET.get('text','default'))
    print(txt)
    tts = gTTS(text=text_to_speak, lang='mr')
    tts.save('media/speechmr.mp3')
    params = {'english':english_translation, 'hindi':hindi, 'marathi':marathi}
    return render(request,'anounce.html',params)

def anounceinmarathi(request):
    text = (request.GET.get('Text','default'))
    print(text)

    def roman_marathi_to_marathi(roman_text):
        # Use Indic Transliteration to convert Romanized Marathi to Devanagari
        marathi_text = sanscript.transliterate(roman_text, sanscript.ITRANS, sanscript.DEVANAGARI)
        return marathi_text

# Example usage
    romanized_text = text
    marathi_text = roman_marathi_to_marathi(romanized_text)

    def translate_to_english(text):
        translator = Translator()
        translated_text = translator.translate(text, src='mr', dest='en')
        return translated_text.text
    english_translation = translate_to_english(marathi_text)
    
    def english_to_marathi(text):
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='mr')
        return translated_text.text
    marathi= english_to_marathi(english_translation)
   
    def translate_to_hindi(text):
        translator = Translator()
        translated_text = translator.translate(text, src='en', dest='hi')
        return translated_text.text
    hindi = translate_to_hindi(english_translation)

    # def translate_to_marathi(text):
    #     translator = Translator()
    #     translated_text = translator.translate(text, src='en', dest='mr')
    #     return translated_text.text

    # marathi = translate_to_marathi(english_translation)


    text_to_speak = english_translation  # Replace with your desired text
    txt = (request.GET.get('text','default'))
    print(txt)
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save('media/speecheng.mp3')
    
    text_to_speak = hindi  # Replace with your desired text
    txt = (request.GET.get('text','default'))
    print(txt)
    tts = gTTS(text=text_to_speak, lang='hi')
    tts.save('media/speechhi.mp3')
    
    text_to_speak = marathi  # Replace with your desired text
    txt = (request.GET.get('text','default'))
    print(txt)
    tts = gTTS(text=text_to_speak, lang='mr')
    tts.save('media/speechmr.mp3')
    params = {'english':english_translation, 'hindi':hindi, 'marathi':marathi}
    return render(request,'anounce.html',params)

