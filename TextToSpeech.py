from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
from gtts import gTTS
from telethon.errors import ForbiddenError
from Alishan import Inishaikhalishan

client = TelegramClient(StringSession(Inishaikhalishan.string), Inishaikhalishan.api_id, Inishaikhalishan.api_hash)


@client.on(events.NewMessage(outgoing=True, pattern=r'(?i).*tts'))
async def handler(event):
    if event.is_reply:
        repliad = await event.get_reply_message()
        sender = repliad.sender 
        tts = gTTS(repliad.message)
        tts.save("TextToSpeech.mp3")
        try:
            await event.respond(file="TextToSpeech.mp3")
        except:
            print(f"Error : Forbidden. the bot cannot send a file to @{sender.username}")
        full_name = f"{sender.first_name} {sender.last_name}" if sender.last_name else sender.first_name
        print(f"{full_name}`s Message Converted To Speech.")
        await event.delete()
    else:
        m = event.message.text
        m1 = event.message
        me = await client.get_me()
        username = me.username
        if len(m) > 4:
            message = m[4 :len(m)]
            tts = gTTS(message)
            tts.save("TextToSpeech.mp3")
            try:
                await event.respond(file="TextToSpeech.mp3")
            except:
                print(f"Error : Forbidden. the bot cannot send a file to @{username}")
            await event.delete( )
            print("Your Message Successfully Converted to Speech.")
        else:
            await m1.reply("After Enterd Command,, Then Some Text Are Required!")
            print("User Not Entered Text.")


client.start()
client.run_until_disconnected()