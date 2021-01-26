import discord
# import requests
import json
from discord.ext import commands

with open('wallet/wallet.json') as f:
  data = json.load(f)


def sendbch():

    url = "https://rest-unstable.mainnet.cash/wallet/send"
    payload="{\"walletId\": \""+data["walletId"]+"\",\"to\": [{\"cashaddr\": \""+data["reciever"]+"\",\"value\":  0.01 ,\"unit\": \"usd\"}]}"
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    # return response.text
    return "Sent"



client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.command()
async def send(ctx):
     print(sendbch())

client.run("ODAyMzg1NjkzMzQ3MDIwODAw.YAud6A.AxIxokhGFc38VJtrxYsZ2sT_zv4")