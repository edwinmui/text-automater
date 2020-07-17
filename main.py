import os
import config

def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words =(text.split())
    return words

def send_message(phone_number, message):
    os.system('osascript send.applescript {} "{}"'.format(phone_number, message))

if __name__ == "__main__":
    words = get_words('spam.txt')
    for word in words:
        send_message(config.PHONE_NUM, word)