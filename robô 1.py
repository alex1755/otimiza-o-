import asyncio
from datetime import datetime, time, timedelta
import pytz
import requests
import json
import logging
import time
from telegram import Bot, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

# Configurações
bot = Bot(token"5923804226:AAHPKmjWYQMUOQIbMVVq0gdpWOUk7kausFQ")
chat_id"5923783365"
url = "https://www.onebra.com/push/luckyme"
tz = pytz.timezone('America/Sao_Paulo')
horarios_pagantes = [time(12, 30), time(18, 30), time(20, 30)]
intervalo = timedelta(minutes=5)
ultima_mensagem_enviada = None

async def main():
    global ultima_mensagem_enviada
    while True:
        agora = datetime.now(tz).time()
        proximo_hp = min(filter(lambda x: x > agora, horarios_pagantes), default=None)

        if proximo_hp:
            hora_inicio = proximo_hp.replace(second=0)
            hora_fim = hora_inicio + intervalo
            hora_inicio_str = hora_inicio.strftime('%H:%M')
            hora_fim_str = hora_fim.strftime('%H:%M')

            if ultima_mensagem_enviada != hora_inicio:
                mensagem = f"🚨 ENTRADA CONFIRMADA 🚨\n\n🐯 Fortune Tiger\n⏰ Estratégia:HoráriosPagantes\n⚠️ Válido das: {hora_inicio_str} há {hora_fim_str}\n🌎 Horário De Brasília\n\n💰 5x Normal\n💰 5x Turbo\n\n⚡ Intercalando\n\n🔗 [Jogar no LuckyMe]({url})"
                keyboard = [[InlineKeyboardButton("Jogar", url=url)]]
                reply_markup = InlineKeyboardMarkup(keyboard)
                await bot.send_message(chat_id=chat_id, text=mensagem, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)
                ultima_mensagem_enviada = hora_inicio
        else:
            if ultima_mensagem_enviada != agora:
                mensagem = f"✅ Sinal Finalizado ✅\n🕑 Finalizado às: {agora.strftime('%H:%M')}"
                await bot.send_message(chat_id=chat_id, text=mensagem)
                ultima_mensagem_enviada = agora

        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
