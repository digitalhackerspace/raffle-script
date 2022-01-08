#!/usr/bin/env python3

import os
import discord
import sys
from discord.utils import get
import random

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

GUILD_ID = 565788276397441025
CHANNEL_ID = 565943840687783966
MESSAGE_ID = 926931935337513011

ADMIN_ROLE_ID = 565793023481348126
REGULAR_ROLE_ID = 600393839370436609

@client.event 
async def on_ready():
	target_guild = client.get_guild(GUILD_ID)
	target_channel = target_guild.get_channel(CHANNEL_ID)
	target_message = await target_channel.fetch_message(MESSAGE_ID)
	admin_role = target_guild.get_role(ADMIN_ROLE_ID)
	regular_role = target_guild.get_role(REGULAR_ROLE_ID)

	for reaction in target_message.reactions:
		print(reaction.emoji, " (" + str(reaction.count) + " reactions)")
		rafle_entrees = []
		users = await reaction.users().flatten()
		for user in users:
			# exclude admins from the raffle
			if admin_role in user.roles:
				continue

			rafle_entrees.append(user.display_name)

			# add second entry for regulars
			if regular_role in user.roles:
				rafle_entrees.append(user.display_name + (" SECOND ENTRY"))


		print("\nentrees: ")
		for entree in rafle_entrees:
			print(entree, "|", end=' ')

		winner = random.choice(rafle_entrees)

		print("\n\n-----------------")
		print(winner + " has won the raffle for", reaction.emoji)
		print("-----------------\n\n")

print("Starting draw...\n\n")
client.run(sys.argv[1])
