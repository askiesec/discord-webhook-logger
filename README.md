# ratPY - Discord SPY

| ratPY | 
| ------------- | 
| ![Alt text](https://media.discordapp.net/attachments/1111073482927771700/1122299275913728120/image.png?width=780&height=408) |

## Requirements before setup:
1. Python 3.11 installed
2. Any text editor(VS Code recommended)

## Setup Script
1. Acess [Discord Web App](https://discord.com)
2. Ctrl+Shift+I to open developer tools from your browser
3. Go to Network tab send any message on chat
4. ![Alt text](https://media.discordapp.net/attachments/1111073482927771700/1122299276148613140/image-1.png?width=418&height=468)
5. On messages search for authorization copy and save your account token(**DON'T SHARE YOUR TOKEN WITH ANYONE**)
6. Create your [Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
7. Copy [channel id](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) from a channel you gonna spy
8. Run the ```run.bat``` file and wait for all the packages to be installed.
9. Navigate to the config folder, right click on the config.json file.
![Alt text](https://media.discordapp.net/attachments/1111073482927771700/1122299276396089414/image-2.png?width=806&height=407)
10. Fill all fields
``` json
"token": "TOKEN ACCOUNT",
"hook": "WEBHOOK LINK",
"channelID": CHANNEL ID WIHOUT QUOTES
```
10. Save and run ```ratpy``` on src folder
