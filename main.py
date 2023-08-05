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
    
    if event.message.fwd_from:
        if event.message.text:
            if "DerivBotManager" not in event.message.text:
                for channel in destination_channels:
                    await client.forward_messages(entity=channel, messages=event.message)
        elif event.message.photo and event.message.caption:
            if "DerivBotManager" not in event.message.caption:
                for channel in destination_channels:
                    await client.forward_messages(entity=channel, messages=event.message)
    elif event.message.text:
        if "DerivBotManager" not in event.message.text:
            print("dllla")
            for channel in destination_channels:
                await client.send_message(entity=channel, message=event.message.text)
    elif event.message.photo and event.message.caption:
        print("Debug - Photo:", event.message.photo)
        print("Debug - Caption:", event.message.caption)
        if "DerivBotManager" not in event.message.caption:
            for channel in destination_channels:
                await client.send_file(entity=channel, file=event.message.photo, caption=event.message.caption)

# Run the client until disconnected
client.run_until_disconnected()
