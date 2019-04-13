import telebot
import pymysql
from telebot import types
import requests

bot = telebot.TeleBot("824295335:AAGK4j81vjcKoRsNd_1mWOwMPafNRfhWqhY")
asd = False
asd1 = False


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global asd
    global asd1
    if message.text == '/start' or message.text == 'Старт':
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT api_key from users WHERE user_id=%s "
        args = (str(name))
        cursor.execute(query, args)
        row = cursor.fetchone()
        print(row)
        conn.close()

        if row != None:
            api_key = str(row[0])
            servstop = "https://cw-serv.ru/api/key/%s/action/start" % api_key
            print(servstop)
            print(api_key)
            r = requests.get(servstop)
            text = ''
            for i in (r.json()).items():
                text = str(i[1])
            print(text)
            if text == 'ok':
                bot.send_message(message.from_user.id, "Выполнено", reply_markup=keyboard())
            else:
                bot.send_message(message.from_user.id, text, reply_markup=keyboard())

        elif asd == False:
            bot.send_message(message.from_user.id, "Введите api key: ")
            asd = True
            print(asd)

        elif asd == True:
            bot.send_message(message.from_user.id, "Введите api key: ")

    elif message.text == "Помощь" or message.text == "/help":
        bot.send_message(message.from_user.id, "Воспользуйтесь специальной клавиатурой снизу или же используйте команды:\n /start\n /stop\n /status \n /load \n /restart \n /update \n P.S На команды можно нажимать :)")

    elif message.text == 'Стоп' or message.text == "/stop":
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT api_key from users WHERE user_id=%s "
        args = (str(name))
        cursor.execute(query, args)
        row = cursor.fetchone()
        print(row)
        conn.close()

        if row != None:
            api_key = str(row[0])
            servstop = "https://cw-serv.ru/api/key/%s/action/stop" % api_key
            print(servstop)
            print(api_key)
            requests.post(servstop)
            bot.send_message(message.from_user.id, "Выполнено", reply_markup=keyboard())
        elif row == None:
            bot.send_message(message.from_user.id, "Для начало работы, Вам нужно нажать на кнопку 'Старт'")

    elif message.text == 'Перезапуск' or message.text == "/restart":
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT api_key from users WHERE user_id=%s "
        args = (str(name))
        cursor.execute(query, args)
        row = cursor.fetchone()
        print(row)
        conn.close()

        if row != None:
            api_key = str(row[0])
            servstop = "https://cw-serv.ru/api/key/%s/action/restart" % api_key
            print(servstop)
            print(api_key)
            r = requests.get(servstop)
            text = ''
            for i in (r.json()).items():
                text = str(i[1])
            print(text)
            if text == 'ok':
                bot.send_message(message.from_user.id, "Выполнено", reply_markup=keyboard())
            else:
                bot.send_message(message.from_user.id, text, reply_markup=keyboard())
        elif row == None:
            bot.send_message(message.from_user.id, "Для начало работы, Вам нужно нажать на кнопку 'Старт'")

    elif message.text == 'Статус' or message.text == "/status":
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT api_key from users WHERE user_id=%s "
        args = (str(name))
        cursor.execute(query, args)
        row = cursor.fetchone()
        print(row)
        conn.close()

        if row != None:
            api_key = str(row[0])
            servstat = "https://cw-serv.ru/api/key/%s/action/data" % api_key
            print(servstat)
            print(api_key)
            r = requests.get(servstat)
            text = ''
            text1 = ''
            for i in (r.json()).items():
                text1 = str(i[1])
                if text1 != 'ключ имеет неправильный формат':
                    if i[0] != 'Игроки:' and i[0] != 'Карта:':
                        if str(i[1]).find(str('Карта:')) != -1:
                            text = text + str(i[0]) + ' ' + str('Включён') + '\n'
                            text = text + str(i[1]) + '\n'
                        elif str(i[1]).find(str('Статус:')) != -1:
                            text = text + str(i[0]) + ' ' + str(i[1][8:-7]) + '\n'
                        else:
                            text = text + str(i[0]) + ' ' + str(i[1]) + '\n'
                            print(i[1])
            if text1 != 'ключ имеет неправильный формат':
                temp = text.find('<')
                temp1 = text.find('>')
                if temp != -1 and temp1 != -1:
                    text = (text[0:temp] + text[temp1+1:-1])
                temp = text.find('<')
                temp1 = text.find('>')
                if temp != -1 and temp1 != -1:
                    text = text[0:temp] + text[temp1+1:]
                print(text)
                bot.send_message(message.from_user.id, text, reply_markup=keyboard())
            else:
                bot.send_message(message.from_user.id, text1, reply_markup=keyboard())
        elif row == None:
            bot.send_message(message.from_user.id, "Для начало работы, Вам нужно нажать на кнопку 'Старт'")

    elif message.text == '/load' or message.text == 'Загрузка':
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT api_key from users WHERE user_id=%s "
        args = (str(name))
        cursor.execute(query, args)
        row = cursor.fetchone()
        print(row)
        conn.close()

        if row != None:
            api_key = str(row[0])
            servstat = "https://cw-serv.ru/api/key/%s/action/load" % api_key
            print(servstat)
            print(api_key)
            r = requests.get(servstat)
            text = ''
            text1 = ''
            for i in (r.json()).items():
                text1 = str(i[1])
                if text1 != 'ключ имеет неправильный формат':
                    text = text + str(i[0]) + ' = ' + str(i[1]) + '\n'
            if text1 != 'ключ имеет неправильный формат':
                print(text)
                bot.send_message(message.from_user.id, text, reply_markup=keyboard())
            else:
                bot.send_message(message.from_user.id, text1, reply_markup=keyboard())
        elif row == None:
            bot.send_message(message.from_user.id, "Для начало работы, Вам нужно нажать на кнопку 'Старт'")

    elif message.text == '/update' or message.text == 'Обновить':
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT api_key from users WHERE user_id=%s "
        args = (str(name))
        cursor.execute(query, args)
        row = cursor.fetchone()
        print(row)
        conn.close()

        if row != None:
            api_key = str(row[0])
            servstat = "https://cw-serv.ru/api/key/%s/action/update" % api_key
            print(servstat)
            print(api_key)
            r = requests.get(servstat)
            text = ''
            for i in (r.json()).items():
                text = str(i[1])
            print(text)
            if text == 'Обновление невозможно, сервер должен быть выключен.':
                bot.send_message(message.from_user.id, 'Выключите сервер и повторите попытку снова.', reply_markup=keyboard())
            elif text == 'ok':
                bot.send_message(message.from_user.id, "Выполнено", reply_markup=keyboard())
            else:
                bot.send_message(message.from_user.id, text, reply_markup=keyboard())
        elif row == None:
            bot.send_message(message.from_user.id, "Для начало работы, Вам нужно нажать на кнопку 'Старт'")

    elif message.text == '/change' or message.text == 'Изменить api key':
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT api_key from users WHERE user_id=%s "
        args = (str(name))
        cursor.execute(query, args)
        row = cursor.fetchone()
        print(row)
        conn.close()

        if row != None:
            bot.send_message(message.from_user.id, "Введите новый api key: ")
            asd1 = True

        elif asd1 == False:
            bot.send_message(message.from_user.id, "Введите api key: ")
            asd = True
            print(asd)

    elif asd1 == True:
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT `user_id` FROM `users` WHERE api_key = %s"
        args = str(message.text)
        cursor.execute(query, args)
        row = cursor.fetchone()

        if row == None:
            query = "UPDATE `users` SET `api_key`= %s WHERE user_id = %s "
            args = str(message.text), (str(name))
            print(args)
            cursor.execute(query, args)
            conn.commit()
            conn.close()
            print(message.text)
            asd1 = False
            bot.send_message(message.from_user.id, "api key - Привязан успешно!", reply_markup=keyboard())
            print(asd)
        else:
            bot.send_message(message.from_user.id, 'Данный api key уже используется!', reply_markup=keyboard())
            asd1 = False

    elif asd == True:
        conn = pymysql.connect('91.134.194.237', 'gs9966', 'STelland3102YT', 'gs9966')
        cursor = conn.cursor()
        name = message.from_user.id
        print(name)
        query = "SELECT `user_id` FROM `users` WHERE api_key = %s"
        args = str(message.text)
        cursor.execute(query, args)
        row = cursor.fetchone()

        if row == None:
            query = "INSERT INTO `users` (`user_id`, `api_key`) VALUES (%s, %s) "
            args = (str(name), str(message.text))
            print(args)
            cursor.execute(query, args)
            conn.commit()
            conn.close()
            print(message.text)
            asd = False
            bot.send_message(message.from_user.id, "api key - Привязан успешно!", reply_markup=keyboard())
            print(asd)
        else:
            bot.send_message(message.from_user.id, 'Данный api key уже используется!', reply_markup=keyboard())
            asd = False

    else:
        bot.send_message(message.from_user.id, "Я Вас не понимаю. Обратитесь за помощью:\n          >>> /help <<<")

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Старт')
    btn2 = types.KeyboardButton('Стоп')
    btn3 = types.KeyboardButton('Перезапуск')
    btn4 = types.KeyboardButton('Статус')
    btn5 = types.KeyboardButton('Загрузка')
    btn6 = types.KeyboardButton('Помощь')
    btn7 = types.KeyboardButton('Обновить')
    btn8 = types.KeyboardButton('Изменить api key')
    markup.add(btn1, btn2)
    markup.add(btn3, btn7)
    markup.add(btn4, btn5)
    markup.add(btn8)
    markup.add(btn6)
    return markup


bot.polling(none_stop=True, interval=0)