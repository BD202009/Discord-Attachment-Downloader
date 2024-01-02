"""
Discord Attachment Downloader v1.0

Developer: Dennis Biehl
Date: January 2, 2024
Description: This script starts the main script discord-attachment-downloader.py

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

import subprocess
import os
import sys
import logging
import traceback
from datetime import datetime

# Set up logging with a custom formatter
log_filename = 'launcher.log'
logging.basicConfig(filename=log_filename, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the working directory to the root folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def start_discord_attachment_downloader():
    # Specify the path to discord-attachment-downloader.py
    script_path = 'src/discord-attachment-downloader.py'
    
    try:
        # Run the script using subprocess and keep the console window open
        subprocess.run(['python', script_path], check=True, shell=True)
    except FileNotFoundError:
        logging.error(f"Error: {script_path} not found.")
        logging.error(traceback.format_exc())  # Log the traceback
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running {script_path}: {e}")
        logging.error(traceback.format_exc())  # Log the traceback
        sys.exit(1)

if __name__ == "__main__":
    start_discord_attachment_downloader()
    sys.exit(0)  # Clean exit
