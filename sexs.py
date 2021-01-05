import discord
import asyncio

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    channel = client.get_channel() ## Insert channel id here. Do not use quotation marks (").

    while not client.is_closed():
      
      if open("text.txt", "r").read() == "1":
            await channel.send("Fuck, get back to lesson.")
            await channel.send(file=discord.File("ss.png"))
            open("text.txt", "w").write("0")
            await asyncio.sleep(1)
            
        else:
            await asyncio.sleep(1)

        if open("text.txt", "r").read() == "2":
            await channel.send("Bip bop. Stopping the bot.")
            open("text.txt", "w").write("0")
            await client.close() ## This gives an error message. But eventually it works ^^

@client.event
async def on_message(message):
    if message.content.find(". help") != -1:
        await message.channel.send("Bip bop. That's why I'm here. My creator <@758788345764773918>")
    if message.content.find(". wtf") != -1:
        await message.channel.send(file=discord.File("ss.png"))

client.loop.create_task(my_background_task())
client.run("") ## Insert token in between.