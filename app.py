import sys
import csv
from flask import Flask, request, jsonify, make_response, send_file
import os
import threading
import pandas as pd
import deepspeech
import wave
import numpy as np
import urllib.request
import soundfile
import ssl
from pydub import AudioSegment


ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False


@app.route("/")
def hello():
    return "Ссылка на запись: <br> <a href=/transcribe/output.txt>Файл</a>"


@app.route('/get', methods=['GET'])
def get_answer2():
    data = request.json
    req = data['new_request']  # идентификатор запроса
    print('req = ', req)
    with open("id_file.csv") as f:
        row_count = sum(1 for line in f)  # количество строк в файле
    if row_count % 2 != 0:
        return make_response(jsonify({"link": "Wait, please"}))
    else:
        f = open('id_file.csv', "r", newline='')
        reader = csv.reader(f)
        read = [["".join(row)] for row in reader]  # запись строк файла в список
        line = read[req + 1]  # последняя строка файла с ссылкой на запись

        return make_response(jsonify({"link": line[0]}))




@app.route('/transcribe', methods=['GET'])
def get_answer():

    data = request.json
    url = data['url']
    user_id = data['user_ID']  # идентификатор пользователя
    extension = data.get('audio_format')  # расширение
    path = "id_file.csv"

    with open("id_file.csv") as f:
        id_number = sum(1 for line in f)  # количество строк
    link_to_download = request.url
    data_r = [[id_number, url, user_id, extension, link_to_download]]
    csv_writer(data_r, path)

    errors(data, extension)  # проверка на ошибки
    th = threading.Thread(target=some_function)
    th.start()

    return make_response(jsonify({"id_number": id_number}))


# обработка для гугловских ссылок
def errors(data, extension):
    if not data or not 'url' in data:
        return make_response(jsonify({"error": "There is no link."}), 400)

    if extension not in ['wav', 'opus', 'mp3']:
        return make_response(jsonify({"error": "The format " + extension + " is not acceptable."}), 400)


def csv_writer(data, path):
    with open(path, "a", newline='\n') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def number_of_channels(w):
    sound = AudioSegment.from_file(w)
    channel_count = sound.channels
    return channel_count


def some_function():
    os.system('python3 transcribation.py')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/transcribe/output.txt', methods=['GET'])  # загрузка файла
def download():
    return send_file('output.txt', attachment_filename="output.txt", as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    threading.Thread(target=app.run).start()
