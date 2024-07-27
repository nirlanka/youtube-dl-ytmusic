import xerox
import yt_dlp as yt

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
  "format": "bestaudio/best",
  "extract-audio": True,
  "audio-quality": 0,
  "audio-format": "mp3",
}

urls = []
url_inp = input("YouTube Music song URL: ")
url_inp = url_inp.replace("music.", "www.")
url_inp = url_inp.split("&")[0]
url_inp = url_inp.strip()
urls = [url_inp]
print()
print("Downloading URLS (modified):")
print(urls)

print()
print("Shell equivalent:")
print("```")
cmd_str = "yt-dlp"

def is_num(x):
    return isinstance(x, (int, float, complex)) and not isinstance(x, bool)

for key in opt:
    v = opt[key]
    if is_num(v):
        v = str(v)
    txt = v if (v == True) else (' \"' + str(v) + "\"") 
    txt = str(txt)
    cmd_str += (' --' + key + txt)
cmd_str += (" \"" + urls[0] + "\"")
print(cmd_str)

print("```")
print()

with yt.YoutubeDL(opt) as ytdl:
    ytdl.download(urls)
