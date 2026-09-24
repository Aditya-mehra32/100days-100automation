import webbrowser
import time

websites = [
    "https://github.com",
    "https://linkedin.com",
    "https://google.com"
]

for site in websites:
    webbrowser.open(site)
    time.sleep(2)
