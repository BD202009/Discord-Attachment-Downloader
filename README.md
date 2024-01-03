# Discord Attachment Downloader v1.0

![](https://github.com/BD202009/Discord-Attachment-Downloader/blob/main/logo/dad-logo.png)

## About

Download attachments from a specified Discord chat or channel. Files will be saved in the format (yyyyMMdd_HHmmss_originalFileName). Additionally, pertinent information such as the message text and sender will be stored in a corresponding txt file.


## Setup

### On a Windows Computer

#### Install Dependencies

1. Install [Visual Studio Community 2022](https://visualstudio.microsoft.com/de/downloads/ "Visual Studio Community") or a later version.
2. Install the Python development workload, including the optional Python native development tools, in Visual Studio Community.
3. Install [Python 3.12](https://www.python.org/downloads/ "Python 3.12") or a later version.

No longer needed, as dependencies will be automatically installed.
- Install the 'discord.py' library using: 
```bash 
pip install discord.py
```

#### Setup a Discord Bot

1. Open [https://discord.com/developers/](https://discord.com/developers/).
2. Navigate to 'Applications' on the left-hand menu and click 'New Application' to add a new application.
3. Name your application (e.g., 'attachment_downloader') and click 'Create.'
4. Choose 'Bot' from the left-hand menu.
5. Click 'Add Bot' and confirm adding a bot to your application by clicking 'Yes, do it!'. Your bot is created now.
6. Click 'Copy' next to the bot icon to copy/note down the bot token. If the 'Copy' button is not visible, click 'Regenerate' first to generate a new bot token.
<span style="color:red;">Do not share the Token!</span>

To use the bot for channels within your server:
1. Navigate to 'OAuth2' and 'URL Generator' via the left-hand menu to generate a permission link.
2. On the following screen, select 'bot' under 'SCOPES' and choose 'Administrator' under 'BOT PERMISSIONS.'
3. Copy and open the 'GENERATED URL' in a new browser window.
4. Choose the server to which the bot should be linked from the drop-down list 'ADD TO SERVER' and click 'Continue.'
5. Click 'Authorize' to confirm the bot's permissions.


## Run the script
1. Clone or download this repository and place it in any folder of your choice on your computer.
2. Run the script by opening either the 'start.py' or 'start.bat' file.
3. During the first run, input your Bot Token; it will be permanently stored in the configuration file.
4. Enter the Discord Server Channel ID from which you want to download attachments. You can confirm or change the Channel ID in each script run.
5. Specify the start and end dates for the attachments. Press 'Enter' to receive all files without date filtering.
6. The script will proceed to download all attachments. If an attachment already exists in the output folder, it will be automatically overwritten.
7. In the output folder, you will find the attachments and corresponding txt-files with the creator's name and message text.



### End
