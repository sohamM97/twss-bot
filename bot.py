# bot.py
import os

import discord
import joblib
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

model = joblib.load('twss_model.sav')

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	text=message.content
	prediction=model.predict([text])[0]
	if prediction==1:
		response = "That's what she said!"
		await message.channel.send(response)

client.run(TOKEN)
