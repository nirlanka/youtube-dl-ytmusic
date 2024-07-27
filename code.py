#!/opt/homebrew/bin/python3

from __future__ import unicode_literals # for youtube_dl

import xerox
import subprocess

import youtube_dl

import credentials

print("""NOTE:
  Copy the cookies in youtube.com or music.youtube.com in Netscape format.
    (Use Cookie-Editor /free/ - https://cookie-editor.com)""")

should_read_cookies = input("Read cookies from clipboard? (y/n): ")

if should_read_cookies == "y":
  file = open("cookies.txt", "w")
  file.write(xerox.paste())
  file.close()

opt = {
  "cookies": "cookies.txt",
  #"username": credentials.username,
  #"password": credentials.password,
  "format": "bestaudio/best",
  "extract-audio": True,
#  "audio-format": "mp3",
  "audio-quality": 0,
}

urls = []
url_inp = input("YouTube Music song URL: ")
url_inp = url_inp.replace("music.", "www.")
url_inp = url_inp.split("$")[0]
urls = [url_inp]
print()
print("Downloading URLS (modified):")
print(urls)

print()
print("Shell equivalent:")
print("```")
print("youtube-dl" \
        + " --cookies cookies.txt" \
        #+ " --username " + opt["username"] \
        #+ " --password \"" + opt["password"] + "\""\
        + " --format " + opt["format"] \
        + " --extract-audio"  \
        + " --audio-quality " + str(opt["audio-quality"]) \
        + " " + urls[0] \
      )
print("```")
print()

with youtube_dl.YoutubeDL(opt) as ydl:
    ydl.download(urls)
