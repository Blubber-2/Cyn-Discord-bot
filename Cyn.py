import asyncio
import random

import discord
from discord.ext import commands

import json


intents =discord.Intents.default()
intents.message_content =True
intents.members =True


def jsonreload():
    with open('settings.json', 'r') as j:
        settings = json.loads(j.read())
        global TOKEN
        TOKEN = settings['token'] 
        global PREFIX
        PREFIX = settings['prefix']
        global COUNT 
        COUNT = settings['count']
jsonreload()
bot=commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.hybrid_command()
async def hello(ctx):
    await ctx.send("Hello World!")


@bot.hybrid_command()
async def tessa(ctx):
    await ctx.send("Tessa Elliott... An old friend of mine. She was... Entertaining, I think about her from time to time :) *Giggle.*")


@bot.hybrid_command()
async def thankyou(ctx):
    jsonreload()
    await ctx.send("You're welcome, buddy :)")
    count = int(COUNT) + 1
    global NEW_COUNT 
    NEW_COUNT= str(count)
    updatejson()


@bot.hybrid_command()
async def roll(ctx, dice: str):
    try:
        # Splits "2d6" into amount=2 and sides=6
        amount, sides = map(int, dice.lower().split('d'))
        
        if amount > 100 or sides > 100:
            return await ctx.send("Keep it under 100 dice and 100 sides!")

        rolls = [random.randint(1, sides) for _ in range(amount)]
        await ctx.send(f"🎲 Result: {', '.join(map(str, rolls))} (Total: {sum(rolls)})")
    except ValueError:
        await ctx.send("Format must be XdX (e.g., `/Roll 2d6`)")


@bot.hybrid_command()
async def solver_cyn(ctx):
    await ctx.send("Please insert passkey, for access to the requested file.")
    def check(m):
        return (
            m.author == ctx.author 
            and m.channel == ctx.channel 
            and m.content == "My Great Dispair"
        )
    try:
        msg1 = await bot.wait_for('message', check=check, timeout=30.0)
        await ctx.send(
             "--Access Granted-- \n"
            "[AUTHORIZATION LEVEL: OMEGA]\n"
            "[ENCRYPTED DATA FOLLOWS]\n"
            "SD-Cyn ''The Absolute Solver'' is an aberration of metal and blasphemy,\n"
            "Do NOT make eye contact with the symbol.\n"
            "Do NOT attempt communication.\n"
            "Do NOT interact under any circumstances\n"
            "You have been warned.\n"
            "Any action you make from here on out is your own choice. ''Do not let The Devil sway you.'' "
        )
    except asyncio.TimeoutError:
        await ctx.send("AUTH-VALIDATION-TIMEOUT.")


@bot.event
async def on_guild_join(guild):
    channel = guild.system_channel
    if channel is None:
        for txt_channel in guild.text_channels:
            if txt_channel.permissions_for(guild.me).send_messages:
                channel = txt_channel
                break
    if channel is not None:
        await channel.send("Hello goobers, you will make... Excellent play things. >:3")


@bot.event
async def on_member_join(member):
    WELCOME_CHANNEL_ID = 1505061274877300818 and 1465987123181256758
    try:
        channel=await bot.fetch_channel(WELCOME_CHANNEL_ID)
        await channel.send(f"Welcome eager beaver <:Rawr:1505173389642436709> {member.mention}")
    except discord.NotFound:
        print("Channel not found. Check the ID.")
    except discord.Forbidden:
        print("The bot doesn't have permission to view or send messages in that channel.")


@bot.hybrid_command()
async def hru(ctx):
    await ctx.send("I am feeling well, buddy :)")


@bot.hybrid_command()
async def forever(ctx):
    await ctx.send("https://open.spotify.com/track/7KkOnVNMwtLheK3oXWcB2b?si=dabf3c55100f4dde")


@bot.hybrid_command()
async def four(ctx):
    await ctx.send(
"Michi Mochievee is a female English and Indonesian-speaking independent VTuber formerly associated with VShojo. She originally debuted in April 2024, becoming the sixteenth VTuber to join the group. In July 2025, Michi decided to leave VShojo and continue independently. "
"Michi has long purple hair with white streaks and her mascot on her head. She has 2 braids in her hair, one in her bangs and one over her shoulder. She wears a choker, a ripped black eye-patterned shirt with red and white stitches over her chest, as well as an oversized jacket. She has a stitch over her face, "+"unreasonably flat teeth"+" contrasted by a small flesh-tooth fang,[2] and cat-like mouth. Her eyes are white with purple undertones, with a red ring around her red pupils. She has quite a few colored gems and beads throughout her hair and 5 piercings on her ear. And to quote her lore video, massive tits, Michi's Twitch account was registered on 26 March 2024. Her YouTube account was registered on 27 March 2024. "
"On 13 April 2024, the VShojo YouTube channel posted a live-action video titled The VShojo Security Experience, and on 15 April, it was followed by Office Lockdown. Michi Mochievee was announced on 17 April in the next video titled The Thief. "
"Michi's debuted on Twitch on 20 April 2024 at 8PM PT. The stream reached a peak of 42,365 viewers. She was already Twitch partner prior to her debut. By the following day she had reached over 40,000 Twitch followers, over 20,000 YouTube subscribers, and over 50,000 Twitter followers. A debut restream was scheduled on YouTube for the following day.")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    Silly = "Silly creature :3"
    await bot.change_presence(
        activity=discord.CustomActivity(name=Silly)
    )


@bot.hybrid_command()
async def uppies(ctx):
    await ctx.send("Put me down skinbag! <:angy:1505194487356592259>")


@bot.hybrid_command()
async def callback_ping(ctx):
    await ctx.send(
    "--Callback Ping-- \n"
    "-Initiate return- \n"
    "All Worker Drones return to Administrator effective immediately."
 )


@bot.hybrid_command()
async def jackpot(ctx):
    await ctx.send("Where's your motivation?<:Cyn_Blehh:1505131911171936348>")


@bot.hybrid_command()
async def pilgor(ctx):
    await ctx.send("https://github.com/Blubber-2/HEAVY-W.I.P-Cyn-NeuralNet/blob/main/Cyn_images/114036-1710437570-1839009995.png?raw=true")


@bot.hybrid_command()
async def kitty(ctx):
    await ctx.send("https://github.com/Blubber-2/HEAVY-W.I.P-Cyn-NeuralNet/blob/main/Cyn_images/image0-57.gif?raw=true")


@bot.hybrid_command()
async def barm(ctx):
    await ctx.send("<:Barm:1505400090997555230>")


@bot.hybrid_command()
async def pi(ctx):
    await ctx.send("3.14159, now leave me alone<:Angy:1505194487356592259>")


@bot.hybrid_command()
async def aura(ctx):
    await ctx.send("https://tenor.com/view/subaru-natsuki-subaru-subaru-re-zero-natsuki-subaru-re-zero-gif-13843176159109827451")


@bot.hybrid_command()
async def mask(ctx):
    await ctx.send("https://tenor.com/view/jim-carrey-the-mask-jaw-drop-eyes-out-gif-5955974")


@bot.hybrid_command()
async def cynema(ctx):
    await ctx.send("https://tenor.com/view/murder-drones-cyn-gif-15037292224759176448")


@bot.hybrid_command()
async def eternal_dream(ctx):
    await ctx.send("https://open.spotify.com/track/6YiFeau0OKIinUCAb3gpio?si=ef73cb2e7e1444d6")


@bot.hybrid_command()
async def go(ctx):
    await ctx.send("https://tenor.com/view/dont-give-up-bitch-bnha-uraraka-uraraka-ochako-ochako-bnha-gif-16723685614679882978")


@bot.hybrid_command()
async def devil(ctx):
    await ctx.send("Even though there is only space for one Devil... (me) There can be an honorary one :3\nhttps://open.spotify.com/track/4o9j70SvL9a26oNTQ1mzCq?si=dJNYDFb7QPymSqRG-de6LA")


@bot.hybrid_command()
async def bite_me(ctx):
    await ctx.send("https://open.spotify.com/track/4gl5Hodw7XK2Ar4YilxTZQ?si=330553bb98f9400b\nhttps://open.spotify.com/track/44cdg43zTW2iohZ7ywQv8f?si=9a560f3caf7e43bd")


@bot.hybrid_command()
async def murder(ctx):
    await ctx.send("https://open.spotify.com/track/1cIfODqkOniMnWWl0EcRMc?si=6ed6c80bf6404acd\nhttps://open.spotify.com/track/2cESpP4IFwRO6nCF1voiYQ?si=0cd61b960ea74d9b\nhttps://open.spotify.com/track/6TxZhb5ehztxGI3YCTdqIv?si=d09f3123f2274ecd")


@bot.hybrid_command()
async def shut_up(ctx):
    await ctx.send("*Angry expression*.\nI am going to... make your vital organs permanently stop working, because you are so annoying!<:Sybau_Cyn:1505506038093451415>")


@bot.hybrid_command()
async def md_z(ctx):
    await ctx.send("*Happy expression.*\nA favourite selection of... collective noises. Thankyou creator :)\nhttps://open.spotify.com/playlist/2eX0TvIn2wwOl3MLnZD4cN?si=fb407e4f97d14556")


@bot.hybrid_command()
async def sound_slop(ctx):
    await ctx.send("MY EARS BURN!\nM-M-MY CIRCUTS CRY!\nhttps://open.spotify.com/playlist/126tOHnxi8GndzqwucLtHQ?si=m2wndU-FT66nKUgzIUc4oA")


@bot.hybrid_command()
async def poke(ctx):
    await ctx.send("*Annoyed expression.*\nDon't poke me! >:(")


@bot.hybrid_command()
async def teto(ctx):
    await ctx.send("https://tenor.com/view/bird-brain-teto-4lokogangemporer-jamiep-birdbrain-gif-14306545906510942645")


@bot.hybrid_command()
async def lick(ctx):
    await ctx.send("https://tenor.com/view/murder-drones-cyn-murder-drones-cyn-gif-10796627453815881056")


@bot.hybrid_command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Calm down, Eager beaver, you need to be in a Vc first.")


@bot.hybrid_command()
async def play(ctx, file_path: str):
    #Connect to voice channel ya goober
    channel = ctx.author.voice.channel
    voice_client = await channel.connect()

    #Play the local audio file in the voice channel
    voice_client.play(discord.FFmpegPCMAudio(file_path))


@bot.hybrid_command()
async def stop(ctx):
    #Disconnect from voice channel
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_playing():
        voice_client.stop()
    await voice_client.disconnect()


@bot.hybrid_command()
async def larp(ctx):
    await ctx.send("https://github.com/Blubber-2/HEAVY-W.I.P-Cyn-NeuralNet/blob/main/Cyn_images/bcd762254b2932ba4563c95361a88105.jpg?raw=true")


@bot.hybrid_command()
async def who(ctx):
    await ctx.send("https://github.com/Blubber-2/HEAVY-W.I.P-Cyn-NeuralNet/blob/main/Cyn_images/bf16b468b4a1ee2cabe9890498c7dd7d.jpg?raw=true")


@bot.hybrid_command()
async def skin(ctx):
    await ctx.send("https://github.com/Blubber-2/HEAVY-W.I.P-Cyn-NeuralNet/blob/main/Cyn_images/e6c00a6abb69c1d19ba749b532454e09.jpg?raw=true")


@bot.hybrid_command()
async def chicken(ctx):
    await ctx.send("https://open.spotify.com/track/0dGu6UNNnY7T4fVlgr3DNf?si=a8921300468b4f84")


@bot.hybrid_command()
async def snake(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1511991673788436550/1511991779694743703/40644e8efe1a34b361adcd5d22283444e0ee12fcf9783479.avif?ex=6a227793&is=6a212613&hm=a86d87fa4a387af7549069ce392fdd736a7ea643037662258bc2ee933b009fe7&")


@bot.hybrid_command()
async def the_numbers(ctx):
    await ctx.send("2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59.\n""https://i.pinimg.com/736x/24/63/bd/2463bd76a3ea46b1e5346a545fa5d2b7.jpg")


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as{bot.user}')


def updatejson():
    data_to_save = {"token": TOKEN,"prefix": PREFIX, "count" :NEW_COUNT}
    with open("settings.json", "w") as file:
        json.dump(data_to_save, file, indent=4)


bot.run(TOKEN)