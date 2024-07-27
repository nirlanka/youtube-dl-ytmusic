#!/opt/homebrew/bin/python3

from __future__ import unicode_literals # for youtube_dl

import xerox
import subprocess

import youtube_dl

print("""NOTE:
    Copy the cookies in youtube.com or music.youtube.com in Netscape format.
        (Use Cookie-Editor /free/ - https://cookie-editor.com)""")

should_read_cookies = input('Read cookies from clipboard? (y/n): ')

if should_read_cookies == "y":
  file = open('cookies.txt', 'w')
  file.write(xerox.paste())
  file.close()

opts = {}

#with youtube_dl.YoutubeDL
