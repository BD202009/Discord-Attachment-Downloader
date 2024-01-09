"""
Discord Attachment Downloader Launcher

This script serves as a launcher for the Discord Attachment Downloader tool.
It checks and installs the required dependencies listed in 'requirements.txt',
then executes the main script for downloading Discord attachments.

Author: Dennis Biehl

Contributors:
- [Contributor 1]
- [Contributor 2]

License:
MIT License

Dependencies:
- subprocess
- os
- sys
- logging
- traceback
- datetime

Usage:
1. Ensure 'requirements.txt' contains the necessary packages.
2. Run this script to check and install dependencies.
3. The main script, 'discord-attachment-downloader.py', will be launched.

Notes:
- Logs are saved to 'launcher.log' with a custom formatter.

Version: __version__
Release Date: __release_date__
Date: 2024-01-03

Updates:
- 2024-01-02: Initial release.
- 2024-01-03: Docstring updated.
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

def read_requirements_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def check_dependencies(required_packages):
    installed_packages = subprocess.check_output([sys.executable, "-m", "pip", "list"]).decode("utf-8").split("\n")
    installed_packages = {line.split("==")[0].lower() for line in installed_packages if line}

    missing_packages = [pkg for pkg in required_packages if pkg.lower() not in installed_packages]
    return missing_packages

def install_dependencies(required_packages):
    missing_packages = check_dependencies(required_packages)

    if missing_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            logging.info("Dependencies installed successfully.")
            print("Dependencies installed successfully.")
        except subprocess.CalledProcessError:
            logging.error("Error installing dependencies. Please install them manually.")
            print("Error installing dependencies. Please install them manually.")
    else:
        logging.info("All dependencies are already installed.")
        print("All dependencies are already installed.")

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
    requirements_file = 'requirements.txt'
    required_packages = read_requirements_file(requirements_file)

    install_dependencies(required_packages)
    
    start_discord_attachment_downloader()
    sys.exit(0)  # Clean exit
