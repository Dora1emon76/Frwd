from telethon import TelegramClient, events, Button
import asyncio

# Set your API ID, API hash, and phone number with country code
api_id = 28558549
api_hash = '7aa7cc23963372ec5bcd5baf56d9817e'
phone_number = '+2348120541489'

client = TelegramClient('session_name', api_id=api_id, api_hash=api_hash)

# Start the client
client.start(phone=phone_number)
print('Client started successfully!')

# Define the channels to forward messages to
destination_channels = ["@binary_GoldForex", "@xaussdForexGoat_Signals", "FXpremiere_freeCrypto"]
source = "@rest516"

@client.on(events.NewMessage(chats=[source]))
async def forward_messages(event):
    print(event.message)
    if event.message.text is not None:
        if "DerivBotManager" not in event.message.text:
            if event.message.fwd_from is None:
                if event.message.photo:
                    for channel in destination_channels:
                        await client.send_file(entity=channel, file=event.message.photo, caption=event.message.text)
                elif event.message.photo is None:
                    for channel in destination_channels:
                        await client.send_message(entity=channel, message=event.message.text)
            else:
                for channel in destination_channels:
                    await client.forward_messages(entity=channel, messages=event.message)
    elif event.message.text is None:
        print("hh")
        if event.message.fwd_from is None:
            if event.message.photo:
                for channel in destination_channels:
                    await client.send_file(entity=channel, file=event.message.photo)
        else:
            for channel in destination_channels:
                await client.forward_messages(entity=channel, messages=event.message)
# Run the client until disconnected
client.run_until_disconnected()
