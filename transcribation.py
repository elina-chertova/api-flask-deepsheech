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

if os.path.isfile("output_graph_1.pbmm"):
    model = deepspeech.Model('output_graph_1.pbmm')
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

# закрыть файл
# 0,https://megapesni.net/download.php?id=225480,Sam Jason1,mp3

'''
file = open('id_file.csv')
line = file.readlines()[0].split(',')  # список данных
id_number = line[0]
url = line[1]
user_id = line[2]  # идентификатор пользователя
extension = str(line[3])  # расширение
link_to_download = line[4]
print(link_to_download[:-1] + '/output.txt')
file.close()'''

with open('id_file.csv', "r", newline='') as f:
    reader = csv.reader(f)
    r = [[",".join(row)] for row in reader]


f = open('id_file.csv')
row_count = sum(1 for line in f)

line = r[row_count - 1][0].split(',')

id_number = line[0]
url = line[1]
user_id = line[2]  # идентификатор пользователя
extension = str(line[3])  # расширение
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
    # os.system("sox " + '--info' + ' audio_for_stt.wav')
    os.rename("audio_for_stt.wav", "old.wav")
    os.system("sox " + '-v 0.95' + ' old.wav' + " -G -r 16000 -c 1 -b 16 " + 'audio_for_stt.wav')
    # -v 0.95 перепроверить (должно решать проблему: sox WARN dither: dither clipped 1 samples; decrease volume?)
    # потери?
    # os.system("sox " + '--info' + ' audio_for_stt.wav')  # данные об итоговом wav файле
    os.remove("old.wav")
    w = wave.open('audio_for_stt.wav', 'r')

frames = w.getnframes()
buffer = w.readframes(frames)
# print(rate)
# print(model.sampleRate())  # частота дискретизации в выборках в секунду данных PCM
# type(buffer)

data16 = np.frombuffer(buffer, dtype=np.int16)
text = model.stt(data16)  # перевод записи в текст

with open("output.txt", "w+") as f:  # запись id пользователя и итогового текста
    f.write(user_id + ': ' + text)
f.close()
link_to_download_n = link_to_download + '/output.txt'


'''os.remove("audio_for_stt.wav")
with open('id_file.csv', 'a') as fd:
    fd.write(link_to_download_n)'''

#fd = open('id_file.csv', 'a')
#fd.write(link_to_download_n)
#fd.close()

with open('id_file.csv', "a", newline='\n') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow([link_to_download_n])
