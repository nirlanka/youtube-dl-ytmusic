#!/opt/homebrew/bin/python3

import xerox

print("""NOTE:
    Copy the cookies in youtube.com or music.youtube.com in Netscape format.
        (Use Cookie-Editor /free/ - https://cookie-editor.com)
""")

should_read_cookies = input('Read cookies from clipboard? (y/n): ')

if should_read_cookies == "y":
  file = open('cookies.txt', 'w')
  file.write(xerox.paste())
  file.close()


