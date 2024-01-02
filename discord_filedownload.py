import discord
import os
from datetime import datetime

# Replace with your bot token
TOKEN = "MTE5MTU3MTE1ODY0Mjk5NTIxMA.GCUmIA.cWtsqv9duNz7okqG279B6EyccN2MhsJNXwbfQI"

# Take user input for the desired channel ID
CHANNEL_ID = input("Enter the Discord channel ID: ")

# Replace with the desired channel ID
#CHANNEL_ID = "1189662073316188231"

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    channel = client.get_channel(int(CHANNEL_ID))
    await download_attachments(channel)

async def download_attachments(channel):
    async for message in channel.history(limit=None):
        for attachment in message.attachments:
            timestamp = get_message_timestamp(message)
            await attachment.save(f"{timestamp}_{attachment.filename}")

def get_message_timestamp(message):
    # Use the timestamp of the message
    timestamp = message.created_at.strftime("%Y%m%d_%H%M%S")
    return timestamp

client.run(TOKEN)

# Notify the user that the code has finished
print("Code has finished. Press any key to close this window.")

# Check if a key is pressed to exit
while True:
    if msvcrt.kbhit():
        msvcrt.getch()
        sys.exit()