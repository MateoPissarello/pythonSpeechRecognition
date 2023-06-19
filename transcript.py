import os
import speech_recognition as sr

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        transcript = recognizer.recognize_google(audio, language="es-ES")
        return transcript
    except sr.UnknownValueError:
        return "No se pudo transcribir el audio"
    except sr.RequestError:
        return "Error en la solicitud al servicio de reconocimiento de voz"

# Ruta al archivo de audio
ruta_carpeta = "C:/Users/User/Documents/coding/xd/audios"
carpetaDeAudios = os.listdir("C:/Users/User/Documents/coding/xd/audios")
contador = 1
for file in carpetaDeAudios:
    audio_file = os.path.join(ruta_carpeta, file)
    transcript = transcribe_audio(audio_file)
    name_audio = "audio" + str(contador)
    output_file_path = f"C:/Users/User/Documents/coding/xd/transcipciones/{name_audio}.txt"
    with open(output_file_path, "w") as file:
        file.write(transcript)
    contador += 1
    print("Transcripción guardada correctamente.")

