import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("어밥봇 도움말로 사용 가능한 명령어를 확인하세요.")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("어밥봇 안녕"):
        await message.channel.send(" > 안녕안녕안녕~~~~~~~")

        
access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
