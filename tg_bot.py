import random
import telegram
import os
import argparse
import time
from dotenv import load_dotenv


def post_to_chanel(token: str, delay_time: int):
    bot = telegram.Bot(token=token)
    dir_with_imgs = 'images'
    while True:
        images_name = os.listdir(dir_with_imgs)
        random_img = random.choice(images_name)
        path = os.path.join(dir_with_imgs, random_img)
        bot.send_document(chat_id='@devmn_test', document=open(path, 'rb'))
        time.sleep(delay_time)


def main():
    token = os.environ['TG_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument('--delay_time', help='enter delay time in hours', type=int)
    args = parser.parse_args()
    delay_time = args.delay_time
    if not delay_time:
        delay_time = 4*3600
    else:
        delay_time *= 3600
    post_to_chanel(token, delay_time)

if __name__ == '__main__':
    load_dotenv()
    main()