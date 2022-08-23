import random
import telegram
import os
import argparse
import time
from dotenv import load_dotenv


def post_to_chanel(token: str, chat_id: str, delay_time: int):
    bot = telegram.Bot(token=token)
    dir_with_imgs = 'images'
    while True:
        images_name = os.listdir(dir_with_imgs)
        random_img = random.choice(images_name)
        path = os.path.join(dir_with_imgs, random_img)
        with open(path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file.read())
        time.sleep(delay_time)

def main():
    token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser()
    parser.add_argument('--delay_time', default=4, help='enter delay time in hours', type=int)
    args = parser.parse_args()
    delay_time = args.delay_time
    attempts_conn = 0
    try:
        post_to_chanel(token, chat_id, delay_time)
    except telegram.error.NetworkError:
        if attempts_conn > 0:
            time.sleep(3)
        attempts_conn += 1
        post_to_chanel(token, chat_id, delay_time)


if __name__ == '__main__':
    load_dotenv()
    main()