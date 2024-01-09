"""
Discord Bot for Downloading Attachments and Saving Messages

This script is a Discord bot that connects to a specified Discord server,
downloads attachments from messages within a given date range, and saves
the corresponding message text in a separate text file. The bot prompts
the user for necessary configuration details such as Discord bot token,
channel ID, and date range.

Author: Dennis Biehl

Contributors:
- [Contributor 1]
- [Contributor 2]

License:
MIT License

Dependencies:
- discord.py
- asyncio
- datetime
- os
- msvcrt
- configparser

Usage:
1. Install required dependencies using `pip install -r requirements.txt`.
2. Run the script and follow the prompts to configure the bot.
3. The bot will download attachments and save message text in the 'output' folder.

Configuration:
- The bot reads configuration details from 'config/config.ini'.
- If the configuration file doesn't exist, it will be created with default values.

Notes:
- The script uses asyncio to handle asynchronous input for date entry.
- Attachments are saved in the 'output' folder.
- Each attachment is saved with a filename containing the timestamp and the original filename.
- Message text is saved in a separate '.txt' file with a similar filename structure.

Version: __version__
Release Date: __release_date__
Date: 2024-01-03

Updates:
- 2024-01-02: Initial release.
- 2024-01-03: Docstring updated.
"""


import discord
import os
import sys
import asyncio
from datetime import datetime, timedelta
import msvcrt
from configparser import ConfigParser

def check_discord():
    try:
        import discord
        print("Discord.py is installed.")
        return True
    except ImportError:
        print("Discord.py is not installed.")
        return False
    
bot_ready_event = asyncio.Event()

# Config folder and file
CONFIG_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'config'))
CONFIG_FILE = os.path.join(CONFIG_FOLDER, 'config.ini')
# Output folder in the root directory
OUTPUT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'output'))

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
    TOKEN = input("Enter your Discord bot token: ")

    # Update config file with the entered Token
    config['Credentials']['Token'] = TOKEN
    with open(CONFIG_FILE, 'w') as config_file:
        config.write(config_file)

# Display current channel ID and ask if the user wants to keep it
if CHANNEL_ID:
    current_channel_id = input(f"Current Discord Channel ID: {CHANNEL_ID}\nDo you want to keep it? (Y/N): ")

    if current_channel_id.lower() == 'n':
        CHANNEL_ID = input("Enter the new Discord Channel ID: ")

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

# Create the output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def validate_date_input(date_str):
    try:
        if date_str:
            datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return False

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    channel = client.get_channel(int(CHANNEL_ID))
    
    # Ask the user for date range
    start_date_str = await async_input("Enter the start date in YYYY-MM-DD format (press Enter for all history): ")
    while not validate_date_input(start_date_str):
        start_date_str = await async_input("Enter a valid start date: ")
        
    end_date_str = await async_input("Enter the end date in YYYY-MM-DD format (press Enter for all history): ")
    while not validate_date_input(end_date_str):
        end_date_str = await async_input("Enter a valid end date: ")

    if start_date_str and end_date_str:
        # Parse start and end dates
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d") + timedelta(days=1)  # Include end date

        await download_attachments(channel, start_date, end_date)
    else:
        await download_attachments(channel)

    # Signal that the bot is ready
    bot_ready_event.set()
    

async def async_input(prompt: str) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, input, prompt)
        
async def download_attachments(channel, start_date=None, end_date=None):
    history_limit = None  # No limit by default

    if start_date and end_date:
        # Set the limit based on the date range
        history_limit = await get_message_limit(channel, start_date, end_date)

    async for message in channel.history(limit=history_limit):
        for attachment in message.attachments:
            timestamp = get_message_timestamp(message)
            message_text = f"Author: {message.author.name}\n"  # Add the username to the message text
            message_text += f"Content: {message.content}\n\n" if message.content else ""  # Add message content if available
            
            # Save attachments in the output folder
            output_filename = f"{timestamp}_{attachment.filename}"
            output_path = os.path.join(OUTPUT_FOLDER, output_filename)
            try:
                await attachment.save(output_path)
            except Exception as e:
                print(f"Error saving attachment: {e}")

            # Save message text in a separate .txt file
            txt_filename = f"{timestamp}_{attachment.filename}.txt"
            txt_path = os.path.join(OUTPUT_FOLDER, txt_filename)
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(message_text)

            print(attachment.filename)

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


try:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Run the bot in the event loop
    loop.create_task(client.start(TOKEN))

    # Wait for the bot to be ready
    loop.run_until_complete(bot_ready_event.wait())

    # Prompt the user to press Enter to close the window
    input("Code has finished. Press 'Enter' to close this window.\n")
except KeyboardInterrupt:
    loop.run_until_complete(cleanup())
finally:
    loop.close()
