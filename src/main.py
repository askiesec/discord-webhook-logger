'''
 * Webhook Spy
 * @author askiesec
'''
import discord
import os
import fade
import json
import time
from discord.ext import commands
from dhooks import Webhook, Embed

bot = commands.Bot(command_prefix="", help_command=None, self_bot=True)

with open("config/config.json") as f:
     config = json.load(f)
     token = config["token"]
     # channelID value has to be a int on config.json
     channelID = config["channelID"]
     hook = Webhook(config["hook"])
     
@bot.event
async def on_ready():
    os.system("title Weebhook Spy" if os.name=="nt" else "TERM_TITLE='Webhook Spy'")
    os.system("cls" if os.name=="nt" else "clear")
    banner = (f"""
    
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣮⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠜⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣴⣦⣼⣿⣿⣅⣀⣁⣀⠠⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⣾⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣀⠑⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⢫⣾⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠤⠄⠀⠀⣤⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡈⠓⠦⡄⠀⠀⠀⠀⠀⡰⠋⣠⣿⡿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⣞⣵⣿⠿⣓⡦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠓⢤⡀⠀⢊⣠⣾⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠺⠤⠤⢴⣾⣿⡿⣁⠈⢉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣩⣶⣿⣿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⣿⣥⠁⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⡟⣡⠊⠀⠀⠀⠀
⠀⠀⠀⠘⢠⣿⣿⣿⡿⢿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⢺⣿⣿⣿⢏⠞⠁⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⠃⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⣠⠞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⣠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣧⠠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠤⠤⠤⠒⠓⠚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣠⣤⣶⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣿⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣷⣤⣴⣶⣶⣶⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⣄⢸⣿⣿⣿⣿⣿⠀⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⠉⢀⣩⣉⡛⠿⠿⣹⣿⣿⣿⣿⣿⠿⣅⣀⠈⢹⣿⣿⣿⣿⣿⢀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⣀⠉⣠⣬⢳⡀⢠⣿⠿⠟⣿⣿⠟⠻⠛⠻⢿⣿⣿⣿⣿⣿⣿⢸⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣤⣀⣀⣀⣿⡄⠙⠛⠾⣧⠀⠀⠀⠞⠋⢁⠀⠐⣻⣿⠀⠘⣿⣿⣿⣿⠣⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⡶⢮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣠⠾⢫⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣻⠿⢣⠀⢠⣿⣿⡿⠃⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣿⣿⣿⣿⣿⣏⣯⡀⢸⣆⣖⠉⠛⢿⣿⣿⣿⣿⣯⡉⣿⠡⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠐⠚⢻⣿⣿⡧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣟⠂⢹⣿⣦⠀⠀⠸⣿⣿⡟⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⠛⠙⣇⣹⣟⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣶⣝⠻⠷⠶⣄⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡖⠒⣒⣒⠦⢤⡸⣷⠀⠀⠀⠀⠀⠀⠀⢠⣿⡟⢹⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⢠⠬⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣶⣿⣿⣿⣶⡅⠸⣗⢶⡄⠀⠀⠀⠀⣼⣿⠇⠘⡆⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⡙⠻⢦⠀⠀⠀⠀⠀⠀⠸⣿⠙⠿⢿⠿⣿⣿⣧⠀⠈⢧⡀⠀⠀⢀⣼⣿⣿⡄⠀⢿⢠⡀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣀⡀⠀⢸⣿⣚⣦⠀⠀⠹⣄⣴⣿⡿⠿⠿⡇⠀⠘⣏⢣⡀⠀⠀⠀⠀⠀⠀
⢠⡿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠳⢤⡀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠺⠛⠁⠈⠳⣄⢠⡎⢉⡿⠁⠀⢀⡻⣄⠀⠸⢆⠙⢦⠀⠀⠀⠀⠀
⠘⢱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡏⠀⡾⠀⠀⢠⡟⠀⠈⠙⠀⠈⢷⠀⠳⡄⠀⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣠⣾⡟⣶⣿⣿⡓⣦⣤⣤⣤⣤⣾⣿⣿⣄⣠⠿⠤⣤⠴⢻⡟⠉⠀⠀⠀⠈⢧⠀⠹⡄⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠀⠀⠉⠙⣿⣿⣿⣷⣼⣏⠙⠻⢿⣿⡿⣷⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣡⢴⣟⢙⣗⠶⠦⠤⠀⠀⢳⡀⢰⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣶⠶⠀⠩⢤⣌⡛⠿⠟⠁⠻⠟⠋⠀⠉⠻⣿⣿⡅⠀⠒⠲⡶⠋⠙⢿⡿⣇⠀⠀⠀⠀⠀⢱⡄⠁⠀
⠀⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠉⣧⠀⠀⠀⠀⠀⠈⠳⣤⡀⠀⠀⠀⣀⣠⠔⠛⠛⢷⡀⠀⠞⠀⠀⠀⠀⢻⣽⡄⠀⠀⠀⠀⠀⢹⡀⠀
⠀⠻⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠲⠤⣝⣦⣀⠀⠀⠀⠀⠀⠁⠙⠲⠤⠀⡀⠀⠀⣷⠀
⠈⢂⠹⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣤⣀⠀⠀⠤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠒⠦⣄⡀⠀⠀⠀⢀⢀⣿⣿⣶⣿⡀
⠀⠀⠀⠙⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠓⠦⠀⠀⠙⠓⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠿⠿⠺⠛⠛⠛⠛⠛⠛⠀
⠀⠀⠀⠠⣈⠻⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠐⠦⠉⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   
        
        [*] Developer: https://github.com/askiesec
        [*] Logged as: {bot.user}
        [*] Running Webhook spy on: #{bot.get_channel(channelID)}
    """)
    faded_banner = fade.pinkred(banner)
    print(faded_banner)

@bot.event
async def on_message(message):
        if message.channel.id == channelID:
            date_format = "%a, %d %b %Y %I:%M %p"
            profurl = f"https://discordapp.com/users/{message.author.id}"
            embed = Embed(
                color=0x546e7a,
                timestamp="now"
            )
            embed.set_author(name=f"{message.author}",
                            icon_url=f"{message.author.avatar.url}")
            embed.set_thumbnail(url=f"{message.author.avatar.url}")
            embed.add_field(name="User ID", value=message.author.id)
            embed.add_field(name="", value=f"[Profile Link]({profurl})")
            embed.add_field(
                name="Created At",
                value=f"{message.author.created_at.date()}",
                inline=True,
            )
            embed.add_field(name="*Joined*",
                            value=message.author.joined_at.strftime(date_format))
            embed.add_field(name="*Message*", value=f"`{message.content}`", inline=False)
            embed.add_field(name="*Channel*", value=f"#{message.channel.name}", inline=False)
            embed.add_field(name="**Disclaimer**", value="> This is tool was made for educational purposes and proof of concepts. I'm not accountable for any unlawful, unprecedented action and any violation of ToS administered by a third party.", inline=True)

            hook.send(embed=embed)

            with open("log.csv", "a", encoding='utf-8') as f:
                f.write(f'[-] {time.strftime(date_format)} {message.author}: {message.content}\n')

bot.run(token)
