import discord
import requests
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

    response = requests.request("POST", url, headers=headers, data=payload)    
    
    return json.loads(response.text)


client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.command()
async def send(ctx):
    response = sendbch()
    if not (response.get('txId') is None):
        await ctx.send("Sent")
        await ctx.send("Transaction Id: "+response["txId"])
    else:
        await ctx.send("Not Sent") 
        await ctx.send("Message: "+response["message"])

client.run("ODAyMzg1NjkzMzQ3MDIwODAw.YAud6A.AxIxokhGFc38VJtrxYsZ2sT_zv4")