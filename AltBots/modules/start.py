from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/caption_marathi_status"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/Marathi_Chatting_143")
    ],
    [
        Button.url("• ʀᴇᴘᴏ •", "https://t.me/Marathi_Chatting_143")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern=""))
@X3.on(events.NewMessage(pattern=""))
@X4.on(events.NewMessage(pattern=""))
@X5.on(events.NewMessage(pattern=""))
@X6.on(events.NewMessage(pattern=""))
@X7.on(events.NewMessage(pattern=""))
@X7.on(events.NewMessage(pattern=""))
@X8.on(events.NewMessage(pattern=""))
@X9.on(events.NewMessage(pattern=""))
@X10.on(events.NewMessage(pattern=""))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [🅢︎нεкнαг•♡](https://t.me/its_Me_Max)**\n\n"
        TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://telegra.ph/file/c831f9a5709407e188635.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
