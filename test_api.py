import requests
import time
from datetime import timedelta
import os

os.environ['NO_PROXY'] = '192.168.133.18'
url = 'https://drive.google.com/file/d/1_vWtJGlIDnf_fvPERKmMfiHpdyGKsFM_/view'
url2 = "https://drive.google.com/file/d/1AZi0a3EBinh5u1L7G6JLqqSgo9PapbuT/view?usp=sharing"
url_new = 'https://megapesni.net/download.php?id=225480'
url4 = 'https://drive.google.com/file/d/18FqUSbp3y9_U_PldYUPVPxJ1pS-pz7gi/view?usp=sharing'
url5 = 'https://drive.google.com/file/d/1k24J-0baMB9oj0W38aoRWx6FloVYv5KM/view?usp=sharing'
url6 = 'https://drive.google.com/file/d/1WUsY97G011tsUY5xR3xq3g7YkWmhTZGD/view?usp=sharing'
url7 = 'https://drive.google.com/file/d/1acznXsZRNMMSXEu5gUQCiIz7XiOXOC3F/view?usp=sharing'
url8 = 'https://drive.google.com/file/d/1xIlUfApmlkGO5NIvz8GB9iibZ7en36S7/view?usp=sharing'
url9 = 'https://drive.google.com/file/d/1whHheba7LWD439QO8qj1JC02ey9aTMuA/view?usp=sharing'
url10 = 'https://drive.google.com/file/d/1n_JvMIGBy5qlUwgXqLM7Y2LqEWXAktad/view?usp=sharing'
url11 = 'https://drive.google.com/file/d/1_cuq8zugq0bDjLBGC3SFpQdaYrZvr8kA/view?usp=sharing'
url12 = 'https://drive.google.com/file/d/1mfxsKJpYNHyn2IOt01ZEyK1u74JyoacS/view?usp=sharing'
url13 = 'https://drive.google.com/file/d/1YKjbOTEqh8x3D0xA2FedTpbh1z7X9J2b/view?usp=sharing'
url14 = 'https://drive.google.com/file/d/1mq_8vrIzCqZu-7KccEAQlO9VZjZEuw88/view?usp=sharing'
url15 = 'https://drive.google.com/file/d/1YaEQAeKadem2zrRfVCdat30ccf_9Pu32/view?usp=sharing'
url16 = 'https://drive.google.com/file/d/1E8JMVcEPmhFQJcPF5-z5RFISgnAGkvNP/view?usp=sharing'
url17 = 'https://drive.google.com/file/d/1VKLK5YZOvTOHyZmkbTxSCgdBZJIIdjKM/view?usp=sharing'
u = 'https://drive.google.com/file/d/1opMPLAotLIzom_UXiN5fQgNtIPlE9F6m/view?usp=sharing'
u1 = 'https://drive.google.com/file/d/1wYzCqXfAEAlEk-eAmZrd6y9iXTQKZ5X_/view?usp=sharing'
u2 = 'https://drive.google.com/file/d/1tSXEULbmMEzpg_L2vJ4hnEbJEUKnm_MX/view?usp=sharing'
#http://pr-webinar.miem.vmnet.top/transcribe
start_time = time.time()
res = requests.get('http://pr-webinar.miem.vmnet.top/transcribe',
                           json={'url': url_new, 'user_ID': 'Sam Jason1', 'audio_format': "mp3"})


# 'http://127.0.0.1:5500/transcribe'
new_res = ''
numeration = 0
while numeration == 0:
    time.sleep(10)
    new_res = requests.get('http://pr-webinar.miem.vmnet.top/get', json={'new_request': res.json()['id_number']})  # ###
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


'''
res = ''
while res == '':
    try:
        res = requests.get('http://127.0.0.1:5500/transcribe',
                           json={'url': url2, 'user_ID': 'Sam Jason1', 'audio_format': "wav"}, timeout=None)
        res.encoding = 'utf-8'
        if res.status_code == 200:
            print(res.json()['link'])
        elif res.status_code == 400:
            print(res.status_code, res.json())
        else:
            print(res.status_code)
    except BaseException:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(100)
        print("Was a nice sleep, now let me continue...")
        continue
'''



"""

start_time = time.time()

url3 = 'https://drive.google.com/file/d/1ygnxpNI-58hSQcoAX0UfCAmJIUywKqya/view?usp=sharing'
url = 'https://drive.google.com/file/d/1_vWtJGlIDnf_fvPERKmMfiHpdyGKsFM_/view'

url2 = "https://drive.google.com/file/d/1AZi0a3EBinh5u1L7G6JLqqSgo9PapbuT/view?usp=sharing"

res = requests.get('http://pr-webinar.miem.vmnet.top/transcribe',
                   json={'url': url_new, 'user_ID': 'Sam Jason', 'audio_format': "mp3"})

res.encoding = 'utf-8'
if res.status_code == 200:
    print(res.json()['link'])
    elapsed_time_secs = time.time() - start_time
    msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
#    print(msg)
# вывести время, прошедшее с начала транскрибации
elif res.status_code == 400:
    print(res.status_code, res.json())
else:
    print(res.status_code)


"""



'''res = ''
while res == '':
    try:
        res = requests.get('http://34.83.206.219:5500/transcribe HTTP/1.1',
                   json={'url': url_new, 'user_ID': 'Sam Jason', 'audio_format': "mp3"})

    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(100)
        print("Was a nice sleep, now let me continue...")
        continue
        
        
        
        
        
        
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
url_new = 'https://megapesni.net/download.php?id=225480'

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

session.get('http://192.168.133.18:5500/transcribe',
                   json={'url': url_new, 'user_ID': 'Sam Jason', 'audio_format': "mp3"})







res = 2
while res == 2:
    try:
        res = requests.get('http://pr-webinar.miem.vmnet.top/transcribe',
                           json={'url': url_new, 'user_ID': 'Sam Jason', 'audio_format': "mp3"})

    except BaseException:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(100)
        print("Was a nice sleep, now let me continue...")
        continue



'''


