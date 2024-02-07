import os
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response


if __name__ == '__main__':
    load_dotenv()
    TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
    print(TOKEN)
    #STEP 1 - bot setup
    intents: Intents = Intents.default()
    intents.message_content = True
    client: Client = Client(intents=intents)
    #STEP 2 - Message Functionality
    async def send_message(message: Message,user_message: str) -> None:
        if not user_message:
            print("No message to send")
            return
        if is_private := user_message[0] == "?":
            user_message = user_message[1:]

        try:
            response: str = get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(f"Error: {e}")
    #STEP 3 - Event Handling
    @client.event
    async def on_ready() -> None:
        print(f'{client.user} has connected to Discord!')
    #STEP 4 - Message Handling
    @client.event
    async def on_message(message: Message) -> None:
        if message.author == client.user:
            return
        username: str = str(message.author)
        usermessage: str = message.content
        channel: str = str(message.channel)
        print(f"{username} said {usermessage} in {channel}")
        await send_message(message, message.content)
    #STEP 5 - Run the bot
    client.run(TOKEN)