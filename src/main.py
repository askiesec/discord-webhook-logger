'''
 * ratPY
 * @author 0x14skie
'''
import discord
import os
import fade
import asyncio
import json
from discord.ext import commands
from dhooks import Webhook, Embed

client = commands.Bot(command_prefix="", self_bot=True)
client.remove_command("help")

"""
Load values from config.json
Dont forget to set this
"""
with open("config/config.json") as f:
     config = json.load(f)
     token = config["token"]
     channelID = config["channelID"] # Int value
     hook = Webhook(config["hook"])

"""
Miscellaneous on_ready function ignore this
i love rats btw
"""
@client.event
async def on_ready():
    os.system("cls") 
    banner = ("""
    
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣏⡦⠤⣤⠽⠤⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠤⠣⢈⠇⠀⠁⣠⡿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠉⠀⠀⠀⠀⠀⢀⡀⠈⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⡀⠀⡰⣯⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⡹⠂⢽⠎⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⠠⠄⠃⣴⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠈⠧⣢⠌⣁⠐⠋⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ratPY v1.0.0
    """)
    status = ("""
    [*] Developer: https://github.com/0x14skie/
    """ + f'[*] Logged as: {client.user}\n    [*] Running Webhook spy on: #{client.get_channel(channelID)}')
    faded_banner = fade.pinkred(banner)
    print(faded_banner)
    faded_status = fade.pinkred(status)
    print(faded_status)

"""
Event to send a embed message via weebhook to channel from your choice
"""
@client.event
async def on_message(message):
        if message.channel.id == channelID:
            date_format = "%a, %d %b %Y %I:%M %p"
            user = message.author
            member = message.author
            embed = Embed()
            embed.set_author(name=f"{message.author}",
                            icon_url=f"{member.avatar.url}")
            embed.set_thumbnail(url=f"{member.avatar.url}")
            embed.add_field(name="user id", value=message.author.id)
            embed.add_field(
                name="created at",
                value=f"{member.created_at.date()}".replace("-", "/"),
                inline=True,
            )
            embed.add_field(name="Joined",
                            value=user.joined_at.strftime(date_format))
            embed.add_field(name="channel", value=message.channel.name)
            embed.add_field(name="message", value=f"{message.content}")

            hook.send(embed=embed)

            with open("log.txt", "a") as f:
                f.write(f'[-] {user.joined_at.strftime(date_format)} {user}: {message.content}\n')
asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.new_event_loop()

client.run(token)