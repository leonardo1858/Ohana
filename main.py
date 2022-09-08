# Our main file.


import speech_recognition as sr

# criar um reconhecedor
r = sr.recognizer()

# abrir microfone para captura
with sr.Microphone() as source:
  while True:
    audio = r.listen(source) # Define microfone como fonte de áudio

    print(r.recognize_google(audio,language='PT'))