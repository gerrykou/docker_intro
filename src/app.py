import datetime
import requests

from pathlib import Path

TIME_STR_FORMAT = '%Y-%m-%d %H:%M'

def print_time():
    now = datetime.datetime.now()
    now_str = now.strftime(TIME_STR_FORMAT)

    now_utc = datetime.datetime.utcnow()
    now_utc_str = now_utc.strftime(TIME_STR_FORMAT)

    print(f'now_str: {now_str}, now_utc_str: {now_utc_str }')

def get_html():
    directory = 'data'
    url ='https://en.wikipedia.org/wiki/Eduardo_Galeano'
    print(f'Request url {url}')
    r = requests.get(url)

    p = Path(directory)
    p.mkdir(exist_ok=True)
    
    with open(f'{directory}/file.html', 'w') as file:
        file.write(r.text)

def main():
    print_time()

if __name__ == '__main__':
    main()
    get_html()
