import googletrans
import speech_recognition 
import gtts 
import playsound 

recognzer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("speek now ")
    voice = recognzer.listen(source)
    text = recognzer.recognize_google(voice,language="hi")
    print(text)


translator = googletrans.Translator()
translation = translator.translator(text,dest="en")
print(translation.text)
convert_audio = gtts.gTTs(translation.text , lang="fr")
convert_audio.save("hello.mp3")
playsound.playsound("hello.mp3")
    
