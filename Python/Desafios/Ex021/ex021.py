#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
from pydub import AudioSegment 
audio = AudioSegment.from_mp3("C:\Users\vitor\Git\guanabara\Python\Desafios\Ex021\Spider-man 2099 sound effect.mp3", format="mp3")
audio.export("saida.mp3", format="mp3")