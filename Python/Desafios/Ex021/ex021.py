#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
import pydub
audio = pydub.AudioSegment.from_mp3("C:\\Users\\vitor\\Downloads\\spiderhomem.mp3", format="mp3")
audio.export("saida.mp3", format="mp3")