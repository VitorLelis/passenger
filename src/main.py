import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from response import talk
import logging

logging.basicConfig(filename='passenger.log', level=logging.INFO, format='%(asctime)s - %(message)s')

#LOAD THE TOKEN
load_dotenv()
__TOKEN = os.getenv('DISCORD_TOKEN')

#BOT SETUP
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    """
    Tasked with generating appropriate responses based on the provided message. 
    If no message is received or an exception occurs, the system will log the incident. 
    Otherwise, it will invoke the 'talk' function to produce a suitable response for the user. 
    """
    if not user_message:
        logging.info("NO MESSAGE")
        return
    
    try:
        response = talk(str(message.content))
        await message.channel.send(response)
    
    except Exception as e:
        logging.info(e)

@client.event
async def on_ready() -> None:
    """Log the Bot's status upon initialization."""
    logging.info(f'{client.user} is up!')

@client.event
async def on_message(message: Message) -> None:
    """
    This function ensures that the bot doesn't respond to its own messages.
    Facilitates the proper handling of incoming messages.
    """
    if message.author == client.user:
        return
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    logging.info(f'[{channel}] {username}: {user_message}')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=__TOKEN)

if __name__ == '__main__':
    main()