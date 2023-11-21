from pydub import AudioSegment

def convertir_mp3_a_wav(archivo_mp3, archivo_wav):
    # Cargar el archivo MP3
    audio = AudioSegment.from_mp3(archivo_mp3)

    # Guardar el archivo en formato WAV
    audio.export(archivo_wav, format="wav")

# Reemplaza 'entrada.mp3' con la ruta de tu archivo MP3 de entrada
# y 'salida.wav' con la ruta donde deseas guardar el archivo WAV resultante.

convertir_mp3_a_wav(r"Juego Parcial\Recursos\sonidos\sonido principal.mp3", "Nuevo-sonido")



