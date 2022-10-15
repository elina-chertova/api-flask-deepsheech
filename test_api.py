import requests
import time
from datetime import timedelta
import os

os.environ['NO_PROXY'] = 'x.x.x.x'

url_new = 'https://megapesni.net/download.php?id=225480'

start_time = time.time()
res = requests.get('http://x.x.x.x/transcribe',
                           json={'url': url_new, 'user_ID': 'Sam Jason1', 'audio_format': "mp3"})

new_res = ''
numeration = 0
while numeration == 0:
    time.sleep(10)
    new_res = requests.get('http://x.x.x.x/get', json={'new_request': res.json()['id_number']})  # ###
    if new_res.json()['link'] != 'Wait, please':
        numeration = 1
    print(new_res.json()['link'])
elapsed_time_secs = time.time() - start_time
msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
print(msg)
new_res.encoding = 'utf-8'
if new_res.status_code == 200:
    print(new_res.json()['link'])
elif new_res.status_code == 400:
    print(new_res.status_code, new_res.json())
else:
    print(new_res.status_code)
