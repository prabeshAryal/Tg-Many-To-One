from telethon import TelegramClient, events
import re
from telethon.sessions import StringSession
import os

#Environment Variables
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_Hash')
string = os.environ.get('session_string')
from_id = os.environ.get('from_ids')
to_id = int(os.environ.get('to_id'))
caption = os.environ.get('every_post_caption')

client = TelegramClient(StringSession(string), api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats = from_id))

async def main(event):
    msg = event.message
    msg = event.message
    msg.raw_text = re.sub("📆 ","", msg.raw_text)
    msg.raw_text = re.sub(r'\d{4}\/\d{2}\/\d{2}|(?:[01]\d|2[0-3]):(?:[0-5]\d):(?:[0-5]\d)|UTC|@[A-Za-z0-9_]+|\#[A-Za-z0-9_]+|\#️⃣|▫️$| :\n|\n\.\n|\.\n\.|follow|via|credit|Follow|Via| - |',"",msg.raw_text)
    msg.raw_text = re.sub(r'📃',"", msg.raw_text)

    msg.raw_text = msg.raw_text + "\n" + caption
    await client.send_message(to_id, msg)

with client:
    client.run_until_disconnected()
