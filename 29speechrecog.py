#initially download pip install SpeechRecognition
#record the audio
#convert it to .wav online
#impoert and proceed babaa

# from email.mime import audio
import speech_recognition as sr
audiofile=("speechrecog.wav")
#use audio as source

r=sr.Recognizer() #initialize the recognizer
with sr.AudioFile(audiofile) as source:
    audio=r.record(source)
#reads audio file

try:
    print("Audio file contents : "+ r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech could not understand audio")
except sr.RequestError:
    print("Couldnt get result from google recognition")
