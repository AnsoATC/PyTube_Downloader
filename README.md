# PyTube Downloader: Simple YouTube Video Downloader with Python and Tkinter GUI
#### Video Demo:  https://youtu.be/b5szqiupRkI
#### Description:
PyTube Downloader is a simple YouTube video downloader with a Python and Tkinter GUI. The project allows users to download YouTube videos by entering the video URL into the provided text box and clicking the "Download" button. The downloader looks for the best possible video quality and downloads it for the user. It also displays the download time in a separate window upon successful download.

The main file of the project is project.py, which contains the GUI implementation using the Tkinter library. It includes the main function for running the GUI application and three additional custom functions:

download_video(entry_field): This function handles the video download process using the pytube library. It checks for invalid or empty URLs and displays an error message if necessary.
extract_video_info(entry_field): This function is a placeholder for future implementation to extract video information such as title, duration, and resolution from the YouTube URL.
show_video_info(video_info): This function is also a placeholder for displaying the extracted video information in a separate window.
To use the PyTube Downloader, the user needs to set the appearance mode and default color theme by calling the set_appearance_mode() and set_default_color_theme() functions from the customtkinter library. The downloader also creates a folder named "youtube_downloads" to store downloaded videos.

The project aims to provide an easy-to-use and beginner-friendly interface for downloading YouTube videos without the need for complex command-line tools or external applications. It utilizes the pytube library for video download and Tkinter for creating the graphical user interface.