import sys
import csv
from flask import Flask, request, jsonify, make_response, send_file
import os
import threading
import deepspeech
import wave
import numpy as np
import urllib.request
import soundfile
import ssl
from pydub import AudioSegment

if os.path.isfile("output_graph.pbmm"):
    model = deepspeech.Model('output_graph.pbmm')
else:
    sys.exit('Нет обученной модели')


def google_disk_links(url, extension):
    file_id_num = url.find("/d/") + 3
    file_id = url[file_id_num: url.find("/", file_id_num)]
    link_to_download = 'https://drive.google.com/uc?export=download&id=' + file_id
    urllib.request.urlretrieve(link_to_download, "audio_for_stt." + extension)  # download url to a local file
    if extension != 'wav':
        convert_to_wav(extension)


def convert_to_wav(type_of_file):
    if type_of_file == 'opus':
        data, samplerate = soundfile.read('audio_for_stt.opus')
        soundfile.write('audio_for_stt.wav', data, samplerate, subtype='PCM_16')

    if type_of_file == 'mp3':
        sound = AudioSegment.from_mp3('audio_for_stt.mp3')
        sound.set_frame_rate(16000)
        sound.export('audio_for_stt.wav', format="wav")

    os.remove("audio_for_stt." + type_of_file)


with open('id_file.csv', "r", newline='') as f:
    reader = csv.reader(f)
    r = [[",".join(row)] for row in reader]


f = open('id_file.csv')
row_count = sum(1 for line in f)

line = r[row_count - 1][0].split(',')

id_number = line[0]
url = line[1]
user_id = line[2] 
extension = str(line[3]) 
link_to_download = line[4]

f.close()

# google_disk_links(url, extension)  # загрузка файлов с гугл диска

urllib.request.urlretrieve(url, "audio_for_stt." + extension)  # download url to a local path
if extension != 'wav':
    convert_to_wav(extension)

w = wave.open('audio_for_stt.wav', 'r')
rate = w.getframerate()  # частота дискретизации

if rate != 16000:
    w.close()
    os.rename("audio_for_stt.wav", "old.wav")
    os.system("sox " + '-v 0.95' + ' old.wav' + " -G -r 16000 -c 1 -b 16 " + 'audio_for_stt.wav')
    os.remove("old.wav")
    w = wave.open('audio_for_stt.wav', 'r')

frames = w.getnframes()
buffer = w.readframes(frames)

data16 = np.frombuffer(buffer, dtype=np.int16)
text = model.stt(data16)  # перевод записи в текст

with open("output.txt", "w+") as f:  # запись id пользователя и итогового текста
    f.write(user_id + ': ' + text)
f.close()
link_to_download_n = link_to_download + '/output.txt'


with open('id_file.csv', "a", newline='\n') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow([link_to_download_n])
