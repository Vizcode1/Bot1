import requests
import telebot

def get_ip_location(ip):
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)
    data = response.json()
    return data

def get_phone_details(phone):
    url = f'https://cocowo.com/web/nama-pemilik-nomor-telepon/wa-cek.php?number={phone}'
    response = requests.get(url)
    data = response.text
    start = data.find('<title>') + len('<title>')
    end = data.find('</title>')
    name = data[start:end]
    return name

import asyncio

async def send_dox(bot, message):
    phone = message.text
    name = get_phone_details(phone)
    ip_data = get_ip_location('METODE GET IP DARI PHONE')
    ip = ip_data['query']
    country = ip_data['country']
    city = ip_data['city']
    await bot.reply_to(message, f'Nama: {name}\nIP: {ip}\nNegara: {country}\nKota: {city}')

import telebot

bot = telebot.TeleBot('6702808694:AAECF_IBSUHlkifFJnu_EyQUarxfMwwv-Y8', threaded=True)

@bot.message_handler(commands=['dox'])
def dox(message):
    bot.reply_to(message, 'Masukkan nomor telepon:')
    bot.register_next_step_handler(message, send_dox)

if __name__ == '__main__':
    bot.polling()