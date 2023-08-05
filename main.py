from telethon import TelegramClient, events, Button
import asyncio

# Set your API ID, API hash, and phone number with country code
api_id = 25866651
api_hash = '0581d6e46af16c717302fe1ab46b4147'
phone_number = '+918092409837'
client = TelegramClient('session_name', api_id, api_hash)

# Start the client
client.start(phone=phone_number)
print('Client started successfully!')

# Define the channels to forward messages to
destination_channels = ["@Rest516", "@rest516"]

@client.on(events.NewMessage(chats=["@rest516"]))
async def forward_messages(event):
    if not event.message.fwd_from:
        if event.message.text and "hello" not in event.message.text.lower():
            await client.forward_messages(entity=destination_channels, messages=event.message)
        elif event.message.photo and event.message.caption and "hello" not in event.message.caption.lower():
            await client.forward_messages(entity=destination_channels, messages=event.message)
        else:
            await event.reply("Message does not meet forwarding conditions.")

# Run the client until disconnected
client.run_until_disconnected()
