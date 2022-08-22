import random
import telegram
import os
import argparse
import time
from dotenv import load_dotenv


def post_to_chanel(dalay_time):
    bot = telegram.Bot(token=os.environ['TG_TOKEN'])
    while True:
        images_name = os.listdir('images')
        random_img = random.choice(images_name)
        bot.send_document(chat_id='@devmn_test', document=open(f'images/{random_img}', 'rb'))
        time.sleep(dalay_time)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--delay_time', help='enter delay time in hours', type=int)
    args = parser.parse_args()
    delay_time = args.delay_time
    if not delay_time:
        delay_time = 4*3600
    else:
        delay_time *= 3600
    post_to_chanel(delay_time)

if __name__ == '__main__':
    load_dotenv()
    main()