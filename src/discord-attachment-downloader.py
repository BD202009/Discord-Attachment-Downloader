"""
Discord Attachment Downloader v1.0

Developer: Dennis Biehl
Date: January 2, 2024
Description: This script downloads attachments from a Discord channel and saves them with a timestamped filename.

MIT License

Copyright (c) 2024 Dennis Biehl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import discord
import os
import sys
import asyncio
from datetime import datetime
import msvcrt
from configparser import ConfigParser

CONFIG_FOLDER = '../config'
CONFIG_FILE = os.path.join(CONFIG_FOLDER, 'config.ini')
OUTPUT_FOLDER = '../output'  # Output folder in the root directory

# Function to create the config file with default values
def create_config():
    config = ConfigParser()
    config['Credentials'] = {'Token': '', 'ChannelID': ''}
    with open(CONFIG_FILE, 'w') as config_file:
        config.write(config_file)

# Check if the config file exists, create it if not
if not os.path.isfile(CONFIG_FILE):
    create_config()

# Read configuration from config.ini
config = ConfigParser()
config.read(CONFIG_FILE)

# Retrieve credentials
TOKEN = config.get('Credentials', 'Token')
CHANNEL_ID = config.get('Credentials', 'ChannelID')

# If Token is missing, prompt the user to enter it
if not TOKEN:
    TOKEN = input("Enter your bot token: ")

    # Update config file with the entered Token
    config['Credentials']['Token'] = TOKEN
    with open(CONFIG_FILE, 'w') as config_file:
        config.write(config_file)

# Display current channel ID and ask if the user wants to keep it
if CHANNEL_ID:
    current_channel_id = input(f"Current Channel ID: {CHANNEL_ID}\nDo you want to keep it? (Y/N): ")

    if current_channel_id.lower() == 'n':
        CHANNEL_ID = input("Enter the new Discord channel ID: ")

        # Update config file with the new Channel ID
        config['Credentials']['ChannelID'] = CHANNEL_ID
        with open(CONFIG_FILE, 'w') as config_file:
            config.write(config_file)
else:
    # Prompt the user to input a new channel ID if it's empty
    CHANNEL_ID = input("Enter the Discord channel ID: ")

    # Update config file with the entered Channel ID
    config['Credentials']['ChannelID'] = CHANNEL_ID
    with open(CONFIG_FILE, 'w') as config_file:
        config.write(config_file)

# Replace with your bot token
#TOKEN = "MTE5MTU3MTE1ODY0Mjk5NTIxMA.GCUmIA.cWtsqv9duNz7okqG279B6EyccN2MhsJNXwbfQI"

# Take user input for the desired channel ID
#CHANNEL_ID = input("Enter the Discord channel ID: ")

# Replace with the desired channel ID
#CHANNEL_ID = "1189662073316188231"

# Create the output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    channel = client.get_channel(int(CHANNEL_ID))
    
    # Ask the user for date range
    start_date_str = input("Enter the start date in YYYY-MM-DD format (press Enter for all history): ")
    end_date_str = input("Enter the end date in YYYY-MM-DD format (press Enter for all history): ")

    if start_date_str and end_date_str:
        # Parse start and end dates
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d") + timedelta(days=1)  # Include end date

        await download_attachments(channel, start_date, end_date)
    else:
        await download_attachments(channel)
        
async def download_attachments(channel, start_date=None, end_date=None):
    history_limit = None  # No limit by default

    if start_date and end_date:
        # Set the limit based on the date range
        history_limit = await get_message_limit(channel, start_date, end_date)

    async for message in channel.history(limit=history_limit):
        for attachment in message.attachments:
            timestamp = get_message_timestamp(message)
            message_text = message.content
            
            # Save attachments in the output folder
            output_filename = f"{timestamp}_{attachment.filename}"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)
            await attachment.save(output_path)

            # Save message text in a separate .txt file
            txt_filename = f"{timestamp}_{attachment.filename}.txt"
            txt_path = os.path.join(OUTPUT_FOLDER, txt_filename)
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(message_text)

def get_message_timestamp(message):
    # Use the timestamp of the message
    timestamp = message.created_at.strftime("%Y%m%d_%H%M%S")
    return timestamp

async def get_message_limit(channel, start_date, end_date):
    # Get the messages within the date range to determine the limit
    async for _ in channel.history(after=start_date, before=end_date):
        pass

    # Calculate the limit based on the date range
    limit_date = min(datetime.utcnow(), end_date)  # Use current time or end_date, whichever is earlier
    limit = await channel.history(after=start_date, before=limit_date).flatten()
    return len(limit)

loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(TOKEN))

# Notify the user that the code has finished
print("Code has finished. Press any key to close this window.")

# Check if a key is pressed to exit
while True:
    if msvcrt.kbhit():
        msvcrt.getch()
        sys.exit()
