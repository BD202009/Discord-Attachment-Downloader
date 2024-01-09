@echo off
rem Discord Attachment Downloader Launcher
rem
rem Developer: Dennis Biehl
rem
rem Contributors: [Contributor 1], [Contributor 2]
rem
rem License: MIT License
rem 
rem Description: This script starts the main script discord-attachment-downloader.py
rem
rem Refer to __version__.py for version information
rem
rem Date: 2024-01-02
rem 
rem Updates:
rem 2024-01-02: Initial release.
rem 2024-01-03: Docstring updated.


rem Display a welcome message to the user
echo.
echo Welcome to the Discord Attachment Downloader!
echo This script will start the main attachment downloader tool.
echo.
echo Please wait while the tool initializes...
echo.

rem Launch the main script
python src/discord-attachment-downloader.py

