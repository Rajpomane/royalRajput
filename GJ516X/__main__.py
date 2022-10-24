import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from 𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀 import LOGGER, app, userbot
from 𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀.core.call import GJ516
from 𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀.plugins import ALL_MODULES
from 𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀").warning(
            "Spotify Client Id & Secret not added, Chutiya Saala ek itni simple cheej nahi laa paaya."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀.plugins" + all_module)
    LOGGER("𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await 𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀.start()
    try:
        await 𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀.stream_call(
            "https://telegra.ph/file/c3a6ac9fcde7bd3703d20.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀").error(
            "[ERROR] - \n\nHey , firstly open telegram and turn on voice chat in Logger Group else fu*k off. If you ever ended voice chat in log group i will stop working and users will fu*k you up."
        )
        sys.exit()
    except:
        pass
    await 𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀.decorators()
    LOGGER("𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀").info("Music Bot Started Successfully, Now Give your girlfriend chumt to @I_LOVE_YOU_PAGAL")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("𝐈𝛕ᷟ͢𝚣⃪ꙴ ⋆‌⃝⁣🥵🖤Hᴀᴄᴋᴇʀ Hᴇᴀʀᴛ❤️⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟⃟𓆩᪵𓆪 ⏤͟͟͞➖⃟🥀").info("Stopping Music Bot, Bhakk Bhosdike (Gaand Maraa Tu)")
