import discord
client=discord.Client()
@client.event
async def on_ready():
    print(client.user.id)
    print("준비되었을 때 할말")
    game=discord.Game("하고 있는 게임")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("명령어"):
        await message.channel.send("봇이 할 말")


client.run("CLIENT SECRET 키")