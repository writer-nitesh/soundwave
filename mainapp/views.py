
from django.shortcuts import render, redirect, HttpResponse
from gtts import gTTS
import string
import random
import os
import shutil


def index_page(request):
    print("hi")
    if request.method == "POST":
        letters = string.ascii_lowercase

        file_name = f"{''.join(random.choice(letters) for i in range(10))}.mp3"

        text = request.POST['text']
        tdl = request.POST['tdl']
        lang = request.POST['lang']

        tts = gTTS(text, lang=lang, tld=tdl)
        tts.save(file_name)

        dir = os.getcwd()
        full_dir = os.path.join(dir, file_name)
        print(dir)
        print(full_dir)

        dest = shutil.move(full_dir, os.path.join(
            dir, "mainapp\static\sound_file"))

        data = {"loc" :file_name}
        return render(request,'download.html',data)

    return render(request, 'index.html')


# from gtts import gTTS
# tts_en = gTTS('hello', lang='en')
# tts_fr = gTTS('bonjour', lang='fr')
# >>>
# with open('hello_bonjour.mp3', 'wb') as f:
#     tts_en.write_to_fp(f)
#     tts_fr.write_to_fp(f)
