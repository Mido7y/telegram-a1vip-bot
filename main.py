from telethon import TelegramClient, events
import random
import asyncio

# بيانات API من my.telegram.org
api_id = 20359405
api_hash = 'e2a9c8c9321bbd6b2bc6cb19db7f60d1'

# توكن البوت من BotFather
bot_token = '7956476198:AAEyk12IPaoU9KgrhkZBSIoFxuVE9iZfZxo'

# الردود التلقائية
responses = [
    "01067630851",
    "01120343568",
    "01286188670",
    "01116950371",
]

# الكلمات المفتاحية المطلوبة
keywords = ["رقم فودافون كاش", "كل واحد 10000جنية", "وقتي", "@AS1_R1"]

# اسم قناة المراقبة
channel_username = "A1VIP"

# الأشخاص اللي هيتبعت لهم الرد
recipients = ["@AS1_R1", "@Mido_R7", "@mido9739"]

# تشغيل البوت
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    msg = event.raw_text
    if any(word in msg for word in keywords):
        reply = random.choice(responses)
        for user in recipients:
            await client.send_message(user, reply)
        print(f"تم إرسال الرد {reply} إلى {', '.join(recipients)} بسبب: {msg}")

print("البوت شغّال ومترقب القناة...")
client.run_until_disconnected() 
