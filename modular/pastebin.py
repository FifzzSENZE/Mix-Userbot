################################################################""" Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot @ CREDIT : NAN-DEV"""################################################################import osimport reimport aiofilesfrom pyrogram import filtersimport asynciofrom gc import get_objectsfrom pyrogram.errors import *from Mix import *pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")__modles__ = "Pastebin"__help__ = """ Help Command Pastebin• Perintah : <code>{0}paste</code> [balas pesan]• Penjelasan : Untuk mengupload teks ke pastebin."""@ky.inline("^paste_an")async def _(c, iq):    teks = "Done Pastebin."    try:        _id = int(iq.query.split()[1])        m = [obj for obj in get_objects() if id(obj) == _id][0]        r = m.reply_to_message        if r.text:            content = str(r.text)        else:            if r.document.file_size > 40000:                return await iq.edit_message_text(f"Kamu hanya dapat melakukan jika file dengan ukuran 40KB.")            if not pattern.search(r.document.mime_type):                return await iq.edit_message_text(f"Hanya file teks.")            doc = await m.reply_to_message.download()            async with aiofiles.open(doc, mode="r") as f:                content = await f.read()            os.remove(doc)        link = await paste(content)        kb = InlineKeyboardMarkup([InlineKeyboardButton("Paste Link", url=link)])        hasil = [            InlineQueryResultPhoto(              photo_url=link,              title="kon",              reply_markup=kb,              caption=teks)]        await c.answer_inline_query(            iq.id,            cache_time=0,            results=hasil,        )    except Exception as e:        LOGGER.warning(f"Error: {e}")@ky.ubot("paste", sudo=True)async def _(c: user, m):    emo = Emojii(c.me.id)    emo.initialize()    if not m.reply_to_message:        return await m.reply_text(f"{emo.gagal} Silahkan balas ke pesan.")    r = m.reply_to_message    if not r.text and not r.document:        return await m.reply_text(f"{emo.gagal} Hanya teks dan dokumen yang didukung.")    m = await m.reply_text(f"{emo.proses} Processing...")    if r.text:        content = str(r.text)    else:        if r.document.file_size > 40000:            return await m.edit(f"{emo.gagal} Kamu hanya dapat melakukan jika file dengan ukuran 40KB.")        if not pattern.search(r.document.mime_type):            return await m.edit(f"{emo.gagal} Hanya file teks.")        doc = await m.reply_to_message.download()        async with aiofiles.open(doc, mode="r") as f:            content = await f.read()        os.remove(doc)    link = await paste(content)    kb = ikb({"Paste Link": link})    try:        x = await c.get_inline_bot_results(            bot.me.username, f"paste_an {m.from_user.id}")        return await c.send_inline_bot_result(          m.chat.id, x.query_id, x.results[0].id)    except Exception as e:            return await m.reply(e)            