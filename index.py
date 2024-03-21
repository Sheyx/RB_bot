import json
import requests
import random
import os

tokenBot = os.getenv('TELEGRAM_BOT_TOKEN')


def handler(event, context):
    try:
        if "body" in event:
            data = json.loads(event["body"])
            print(data)
            if "message" in data:
                fromMessage = data['message']
                if "text" in fromMessage:
                    message = ''.join(filter(str.isalnum, fromMessage['text'])).lower().replace("\xc2\xa0", "")
                    print(message)
                    data = {"chat_id": fromMessage['chat']['id'], 'reply_to_message_id': fromMessage['message_id']}

                    title = ''

                    if "title" in fromMessage['chat']:
                        title = fromMessage['chat']['title']

                    if message == 'да' or message == 'if':
                        if getRandom(5) and title == 'REBELS':
                            data['text'] = "@Basil_MrX ты знаешь что делать!"
                            sendToBot('sendMessage', data)
                        elif getRandom(10):
                            data['text'] = "Вы забываете правило ДА?"
                            sendToBot('sendMessage', data)
                        else:
                            data['sticker'] = getPizdaSticker()
                            sendToBot('sendSticker', data)

                    elif message == 'пизда':
                        if getRandom(3):
                            data['text'] = getMessageAnswerPizda()
                            sendToBot('sendMessage', data)

                    elif message == 'start':
                        data[
                            'text'] = 'ВНИМАНИЕ! Бот может непоправимо травмировать вашу психику. Если вы согласны с условиями использования бота напишите "ДА" в ответном сообщение'
                        sendToBot('sendMessage', data)

        r = {'statusCode': 200, 'body': 'Message send'}


    except Exception as e:
        r = {'statusCode': 404, 'body': 'Same error'}

    return r


def sendToBot(type, data):
    r = 'Not send'
    allowtypes = ['sendMessage', 'sendSticker']
    if type in allowtypes:
        url = f"https://api.telegram.org/bot{tokenBot}/{type}"
        r = requests.post(url, data=data)
    return r


def getPizdaSticker():
    sticker = [
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAANQZfliNX5TzTlbiVWLKg3GhqCRRKwAAjUqAALm9vlJKp5EtAAB5dspNAQ',
        'CAACAgIAAxkBAAEEMXVl-zwWr0XgF-CVpziOphw5lg-3kAACxBIAAkOVmUpPyf4zUm0dLTQE',
        'CAACAgQAAxkBAAEEMYll-z2BGOzo6nTQHQIdEe3ffyW9cQAC3QMAAj72Fwd0FUpFbL3jWjQE'
    ]
    return random.choice(sticker)


def getRandom(i):
    if random.randint(1, i) == 1:
        return True
    return False


def getMessageAnswerPizda():
    message = [
        'В жопе у тебя звезда!',
        'В твоём анусе звезда!',
        'в жопе едут поезда!',
        '100 очков ГРИФФИНДОР этому господину!!!'
    ]
    return random.choice(message)
