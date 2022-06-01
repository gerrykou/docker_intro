import datetime


TIME_STR_FORMAT = '%Y-%m-%d %H:%M'

def print_time():
    now = datetime.datetime.now()
    now_str = now.strftime(TIME_STR_FORMAT)

    now_utc = datetime.datetime.utcnow()
    now_utc_str = now_utc.strftime(TIME_STR_FORMAT)

    print(f'now_str: {now_str}, now_utc_str: {now_utc_str }')

def main():
    print_time()

if __name__ == '__main__':
    main()