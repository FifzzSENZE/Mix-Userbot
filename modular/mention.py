import asyncio
import random

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from Mix import *

__modles__ = "Mention"
__help__ = get_cgr("help_mention")

jalan = False
status_per_grup = {}


def random_emoji():
    emojis = "⌚️ 📱 📲 💻 ⌨️ 🖥 🖨 🖱 🖲 🕹 🗜 💽 💾 💿 📀 📼 📷 📸 📹 🎥 📽 🎞 📞 ☎️ 📟 📠 📺 📻 🎙 🎚 🎛 🧭 ⏱ ⏲ ⏰ 🕰 ⌛️ ⏳ 📡 🔋 🪫 🔌 💡 🔦 🕯 🪔 🧯 🛢 🛍️ 💸 💵 💴 💶 💷 🪙 💰 💳 💎 ⚖️ 🪮 🪜 🧰 🪛 🔧 🔨 ⚒ 🛠 ⛏ 🪚 🔩 ⚙️ 🪤 🧱 ⛓ ⛓️‍💥 🧲 🔫 💣 🧨 🪓 🔪 🗡 ⚔️ 🛡 🚬 ⚰️ 🪦 ⚱️ 🏺 🔮 📿 🧿 🪬 💈 ⚗️ 🔭 🔬 🕳 🩹 🩺 🩻 🩼 💊 💉 🩸 🧬 🦠 🧫 🧪 🌡 🧹 🪠 🧺 🧻 🚽 🚰 🚿 🛁 🛀 🧼 🪥 🪒 🧽 🪣 🧴 🛎 🔑 🗝 🚪 🪑 🛋 🛏 🛌 🧸 🪆 🖼 🪞 🪟 🛍 🛒 🎁 🎈 🎏 🎀 🪄 🪅 🎊 🎉 🪩 🎎 🏮 🎐 🧧 ✉️ 📩 📨 📧 💌 📥 📤 📦 🏷 🪧 📪 📫 📬 📭 📮 📯 📜 📃 📄 📑 🧾 📊 📈 📉 🗒 🗓 📆 📅 🗑 🪪 📇 🗃 🗳 🗄 📋 📁 📂 🗂 🗞 📰 📓 📔 📒 📕 📗 📘 📙 📚 📖 🔖 🧷 🔗 📎 🖇 📐 📏 🧮 📌 📍 ✂️ 🖊 🖋 ✒️ 🖌 🖍 📝 ✏️ 🔍 🔎 🔏 🔐 🔒 🔓".split(
        " "
    )
    return random.choice(emojis)


@ky.ubot("tagall", sudo=True)
async def tag_all_members(c: nlx, m):
    chat_id = m.chat.id
    if chat_id not in status_per_grup:
        status_per_grup[chat_id] = {
            "jalan": False,
            "mentioned_count": 0,
            "total_members": [],
        }

    status = status_per_grup[chat_id]

    if status["jalan"]:
        await m.reply("Sedang ada proses tagall/mention lain yang sedang berlangsung.")
        return

    status["jalan"] = True
    status["mentioned_count"] = 0
    status["total_members"] = []

    progres = await m.reply("Sedang proses tagall/mention seluruh member grup ...")

    async for member in c.get_chat_members(chat_id):
        user = member.user
        if not user.is_bot and not user.is_self and not user.is_deleted:
            status["total_members"].append(user.id)

    if not m.reply_to_message and len(m.command) < 2:
        await progres.edit("Silahkan beri pesan atau balas pesan.")
        status["jalan"] = False
        return

    text = await c.get_text(m)
    mention_texts = []

    for member_id in status["total_members"]:
        if not status["jalan"]:
            break
        mention_texts.append(f"[{random_emoji()}](tg://user?id={member_id})")
        status["mentioned_count"] += 1
        if len(mention_texts) == 4:
            mention_text = f"{text}\n\n{' ★ '.join(mention_texts)}"
            try:
                await c.send_message(chat_id, mention_text)
                await asyncio.sleep(3)
            except FloodWait as e:
                tunggu = int(e.value)
                if tunggu > 200:
                    status["jalan"] = False
                    await c.send_message(
                        chat_id,
                        f"Gagal melakukan mention karena waktu tunggu terlalu lama: `{tunggu}` detik.",
                    )
                    return
                await asyncio.sleep(tunggu)
                await c.send_message(chat_id, mention_text)
                await asyncio.sleep(3)
            mention_texts = []

    if mention_texts:
        mention_text = f"{text}\n\n{' ★ '.join(mention_texts)}"
        try:
            await c.send_message(chat_id, mention_text)
            await asyncio.sleep(3)
        except FloodWait as e:
            tunggu = int(e.value)
            if tunggu > 200:
                status["jalan"] = False
                await c.send_message(
                    chat_id,
                    f"Gagal melakukan mention karena waktu tunggu terlalu lama: `{tunggu}` detik.",
                )
                return
            await asyncio.sleep(tunggu)
            await c.send_message(chat_id, mention_text)
            await asyncio.sleep(3)

    status["jalan"] = False
    await progres.delete()
    await c.send_message(
        m.chat.id,
        f"Berhasil melakukan mention kepada <code>{status['mentioned_count']}</code> anggota dari total <code>{len(status['total_members'])}</code> anggota.",
    )


@ky.ubot("stop|cancel")
async def _(c: nlx, m):
    chat_id = m.chat.id
    if chat_id not in status_per_grup:
        status_per_grup[chat_id] = {
            "jalan": False,
            "mentioned_count": 0,
            "total_members": [],
        }

    status = status_per_grup[chat_id]

    if not status["jalan"]:
        await m.reply("Tidak ada proses TagAll/Mention yang sedang berlangsung.")
        return

    status["jalan"] = False
    await m.reply(f"Proses Tag All/Mention berhasil dihentikan.")
