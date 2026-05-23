import os
import discord
from discord.ext import commands
import yfinance as yf
import requests

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "/" , intents = intents)

@bot.event
async def on_ready():
    print("ok")
    user = await bot.fetch_user(1349445955195506781)
    await user.send("UwU Endexx")

def recup():
    ticker = yf.Ticker('AC.PA').info
    market_price = ticker['regularMarketPrice']
    buy_price_per_action = 39.50
    action_number = 10
    buy_total = 0
    gain = 0

    buy_total = buy_price_per_action * action_number + 8.61
    gain_raw = market_price * action_number
    gain = gain_raw - buy_total
    final_gain = gain - gain * (30/100)
    return buy_total, market_price, gain_raw, gain, final_gain

@bot.command()
async def bourse(ctx):
    user = await bot.fetch_user(1349445955195506781)
    buy_total, market_price, gain_raw, gain, final_gain = recup()
    await user.send(f"total buy: {buy_total}")
    await user.send(f"Market Price: {market_price}")
    await user.send(f"gain raw: {gain_raw}")
    await user.send(f"gain: {gain}")
    await user.send(f"final: {final_gain}")

@bot.command()
async def weather(ctx):
    user = await bot.fetch_user(1349445955195506781)
    api_key = "c1cc87c3e7b61f1ca21a22292825ad35"
    city = "Toulouse"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fr"

    response = requests.get(url)

    data = response.json()

    await user.send(f"Température : {data['main']['temp']}°C")
    await user.send(f"Météo : {data['weather'][0]['description']}")


bot.run(token=token)