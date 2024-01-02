# DiscordDownloader

## About

Download attachments from a designated Discord chat or channel. Files will be saved in the format (yyyyMMdd_HHmmss_originalFileName).


## Setup

### On Windows

#### 1. Install the dependencies

- Install [Visual Studio Community 2022](https://visualstudio.microsoft.com/de/downloads/ "Visual Studio Community") or a later version.
- Install the Python development workload, including the optional Python native development tools, in Visual Studio Community.
- Install [Python 3.12](https://www.python.org/downloads/ "Python 3.12") or a later version.
- Download the 'discord_filedownload.py' file from this repository and copy it to any folder of your choice on your computer.
- Install the 'discord.py' library using: 
```bash 
pip install discord.py
```

#### 2. Setup a Discord Bot

- Open [https://discord.com/developers/](https://discord.com/developers/).
- Go to 'Applications' and click on 'New Application' to add a new application.
- Name your application e.g. 'attachement_downloader'. Click on 'Create'
- 

#### 3. Final Setup
- Download the 'discord_filedownload.py' file from this repository and copy into any folder of your choice on your computer.
- Open the 'discord_filedownload.py' file in an editor of your choice
- Add your Bot Token to the script, save and close the file

#### Run the script
- Run the script file via double click or with CMD and the specific commands
- A input will pop up and asks for your channel ID. Enter your Discord channel ID from which you want to save all the files. Press ok. Now all files will be downloaded.

###End
