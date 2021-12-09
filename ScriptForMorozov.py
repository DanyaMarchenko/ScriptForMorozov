import telebot
import time
import pyautogui
import argparse
import sys
import traceback
from PIL import ImageGrab
import datetime

parser = argparse.ArgumentParser(description='Screenshot sender')
parser.add_argument("-d", "--delay", help="The delay in minutes", type=float)
parser.add_argument("-i", "--id", help="The id to where the bot will send screenshots", type=str)
parser.add_argument("-p", "--token", help="The telegram bot token", type=str)

args = parser.parse_args()

minutes = round(args.delay, 1)
id = args.id
token = args.token

def first_get():
    ScreenShot = ImageGrab.grab(xdisplay=1)

    return ScreenShot

def secound_get():
    ScreenShot = ImageGrab.grab(xdisplay=2)

    return ScreenShot

bot = telebot.TeleBot(token)

sending = False

@bot.message_handler(commands=["startscript"])
def start(message):
    print(f"{datetime.datetime.today().strftime('[%H.%M.%S] Start')}")


    global sending
    sending = True
    time_counter = 0

    while sending:

        if time_counter % minutes == 0:

            first_screen = first_get()
            secound_screen = secound_get()

            bot.send_photo(id, screen, caption="1's screen")
            print(f"{datetime.datetime.today().strftime('[%H.%M.%S] The first screenshot has been sent')}")

            bot.send_photo(id, screen, caption="2's screen")
            print(f"{datetime.datetime.today().strftime('[%H.%M.%S] The second screenshot has been sent')}")

            time_counter = 0

        time_counter += 0.1
        time.sleep(10)

@bot.message_handler(commands=["stopscript"])
def stop(message):
    print(f"{datetime.datetime.today().strftime('[%H.%M.%S] Stop')}")

    global sending
    sending = False

bot.polling(none_stop=True)