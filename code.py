import xerox
import yt_dlp as yt

print("""NOTE:
  Copy the cookies in youtube.com or music.youtube.com in Netscape format.
    (Use Cookie-Editor /free/ - https://cookie-editor.com)
""")

should_read_cookies = input("Read cookies from clipboard? (y/n): ")

if should_read_cookies == "y":
  file = open("cookies.txt", "w")
  file.write(xerox.paste())
  file.close()

urls = []
url_inp = input("YouTube Music song URL: ")
is_music = ('music.' in url_inp)

url_inp = url_inp.replace("music.", "www.")
url_inp = url_inp.split("&")[0]
url_inp = url_inp.strip()
urls = [url_inp]

print("""
Downloading URLS (modified):
{}
""".format(urls))

opt = {}
opt["cookies"] = "cookies.txt"
opt["format"] = "bestaudio/best"
if is_music:
    opt["extract-audio"] = True
    opt["audio-quality"] = 0
    opt["audio-format"] = "mp3"

cmd_str = "yt-dlp"

def is_num(x):
    return isinstance(x, (int, float, complex)) and not isinstance(x, bool)

for key in opt:
    v = opt[key]
    if is_num(v):
        v = str(v)
    txt = v if (v == True or v == False) else (' \"' + str(v) + "\"") 
    txt = str(txt)
    cmd_str += (' --' + key + txt)

cmd_str += (" \"" + urls[0] + "\"")

print("""
    Shell equivalent:
    ```
    {}
    ```
""".format(cmd_str))

with yt.YoutubeDL(opt) as ytdl:
    ytdl.download(urls)
