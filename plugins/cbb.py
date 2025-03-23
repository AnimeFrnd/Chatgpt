#(©)Yugen_Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, HELP_MSG, OWNER
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        abt_msg=f"<b>⟦★⟧ Hi There {mention}</b>!💫\n<b>┏━━━━━━━❪❂❫━━━━━━━━</b>\n◈ <b>ᴄʀᴇᴀᴛᴏʀ</b>: <b><a href="https://t.me/rai_yan_00">Rᴀɪ Yᴀɴ</a></b>\n◈ <b>ꜰᴏᴜɴᴅᴇʀ ᴏꜰ</b>: <b><a href="https://t.me/Ani_Weebs">ᴀɴɪᴍᴇ ᴡᴇᴇʙs</a></b>\n◈ <b>ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ</b>: <b><a href="https://t.me/Ongoing_Ani_Weebs">ᴏɴɢᴏɪɴɢ ᴡᴇᴇʙs</a></b>\n◈ <b>Lɪʙʀᴀʀʏ</b>: <b><a href="https://pyrogram.org">Pyʀᴏɢʀᴀᴍ</a></b>\n◈ <b>ᴍʏ ꜱᴇʀᴠᴇʀ</b>: <b><a href="https://render.com">Rᴇɴᴅᴇʀ</a></b>\n◈ <b>ᴅᴇᴠᴇʟᴏᴘᴇʀ</b>: <b><a href="https://t.me/voatcb">VØAT</a></b>\n<b>┗━━━━━━━❪❂❫━━━━━━━━</b>"
        ABOUT_TXT = abt_msg.format(mention=query.from_user.mention)
        await query.message.edit_text(
            text = ABOUT_TXT,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    
                    [
                    InlineKeyboardButton("😔 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = HELP_MSG,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("😔 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
        
        
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


