# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="AlexaOne",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="AlexaTwo",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="AlexaThree",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="AlexaFour",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="AlexaFive",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant Clients...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("Alexa_Help")
                await self.one.join_chat("TheTeamAlexa")
                await self.one.join_chat("Alexa_BotUpdates")
            except Exception:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = get_me.first_name + " " + get_me.last_name
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("Alexa_Help")
                await self.two.join_chat("TheTeamAlexa")
                await self.two.join_chat("Alexa_BotUpdates")
            except Exception:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = get_me.first_name + " " + get_me.last_name
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("GARUD_SUPPORT")
                await self.three.join_chat("OFFICIAL_MAMBA_SUPPORT")
                await self.three.join_chat("MAMBA_GENUINE_SERVICES_CHAT")
            except Exception:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = get_me.first_name + " " + get_me.last_name
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("GARUD_SUPPORT")
                await self.four.join_chat("OFFICIAL_MAMBA_SUPPORT")
                await self.four.join_chat("MAMBA_GENUINE_SERVICES_CHAT")
            except Exception:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = get_me.first_name + " " + get_me.last_name
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("GARUD_SUPPORT")
                await self.five.join_chat("OFFICIAL_MAMBA_SUPPORT")
                await self.five.join_chat("MAMBA_GENUINE_SERVICES_CHAT")
            except Exception:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = get_me.first_name + " " + get_me.last_name
            else:
                self.five.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")
