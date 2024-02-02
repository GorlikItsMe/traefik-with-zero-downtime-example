import requests
from datetime import datetime
from time import sleep


def log(msg):
    dt_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{dt_str}] {msg}')


def test():
    try:
        r = requests.get('http://127.0.0.1/', headers={
            'Host': 'app.localhost'
        }, timeout=1)
        if r.status_code != 200:
            log(f'ERROR_CODE: {r.status_code}')
            return False
        return True
    except requests.exceptions.ReadTimeout:
        log('TIMEOUT')
        return False
    except requests.exceptions.ConnectionError:
        log('CONNECTION_ERROR')
        return False


last_status = False
while True:
    sleep(0.1)
    state = test()
    if state != last_status:
        log(f'App state changed to {state}')
        last_status = state
