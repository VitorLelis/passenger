import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from response import talk

#LOAD THE TOKEN
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#BOT SETUP
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

#LET'S TALK
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("NO MESSAGE")
        return
    
    try:
        response = talk(str(message.content))
        await message.channel.send(response)
    
    except Exception as e:
        print(e)

#BOT STARTUP
@client.event
async def on_ready() -> None:
    print(f'{client.user} is up!')

#MESSAGES HANDLING
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: {user_message}')
    await send_message(message, user_message)

#MAIN
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()