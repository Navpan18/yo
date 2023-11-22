# complete code found in create_basic_tor_proxy.py
import io
import os
import stem.process
import re
import requests
import json
from datetime import datetime
import subprocess

# URL of the video you want to download
video_url = "https://www.youtube.com/watch?v=wYgaOmkNn1M"
SOCKS_PORT = 9050
TOR_PATH = os.path.normpath(os.getcwd()+"\\tor\\tor.exe")
tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
  },
  init_msg_handler = lambda line: print(line) if re.search('Bootstrapped', line) else False,
  tor_cmd = TOR_PATH
)
PROXIES = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}
response = requests.get("https://api.ipify.org?format=json", proxies=PROXIES)
result = json.loads(response.content)
print(result)
proxy_url=PROXIES['http']
subprocess.run(["yt-dlp","-g","-f","22", "--proxy",proxy_url, video_url])
tor_process.kill()
