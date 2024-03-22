from kaggle import KaggleApi

import discord
import asyncio
from discord import app_commands

token = "MTIxNDUyMzQzMzA1MzA2MTE5MA.GXe1XW.TsdrTd8dLJYdfrwMEzwvwlGS_83iXpjh_tYvcM"

MY_GUILD = discord.Object(id=1214464623953321984)
class MyClient(discord.Client):
  def __init__(self,*,intents:discord.Intents):
    super().__init__(intents=intents)
    self.tree = app_commands.CommandTree(self)
  async def setup_hook(self):
      self.tree.copy_global_to(guild=MY_GUILD)
      await self.tree.sync(guild=MY_GUILD)

intent = discord.Intents.default()
intent.message_content = True
intent.members = True
client = MyClient(intents=intent)

@client.event
async def on_ready():
  print("botが起動しました。")

@client.event
async def on_member_join(member):
  print(f"{member.name}参戦")
  user = await client.fetch_user(member.id)
  await user.send("舐め放題ペにペに")
  


@client.event
async def on_message(messages):
  if messages.content == "kaggle-ranking-list":
    competitions = api.competitions_list(search='titanic')
    for competition in competitions:
      print(competition.ref)

api = KaggleApi()
api.authenticate()
print(type(api))

client.run(token)
