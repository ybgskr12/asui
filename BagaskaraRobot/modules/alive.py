import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from BagaskaraRobot.events import register
from BagaskaraRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/a589fe0ca2b883b7a3dc3.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hello guys!! [{event.sender.first_name}](tg://user?id={event.sender.id}), Gua ʙᴀɢᴀsᴋᴀʀᴀ ʀᴏʙᴏᴛ.** \n\n"
  TEXT += "🔰 **Via aktif sekarang** \n\n"
  TEXT += f"🔰 **My Master : [Erna X Bagaskara](https://t.me/ybgskr)** \n\n"
  TEXT += f"🔰 **Library Version :** `{telever}` \n\n"
  TEXT += f"🔰 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"🔰 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Makasih yaa!! Sudah Mau Pakai Erna X Bagaskara Disini 🙏**"
  BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/loveisfuckedup"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/allfucek"),
        ]
    ]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
