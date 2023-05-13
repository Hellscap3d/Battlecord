import discord,json
from commands import classes
import database

rawCommands = classes.command_objects

class Battlecord(discord.Client):
    def __init__(self,config,rawcmds):
        self.config = json.loads(open(config).read())
        self.commands = []
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.database = database.Database("Battlecord.db")
        for command in rawcmds:
            command = command(self)
            self.commands.append(command)
            print(f"Registered {command.name}")
        self.run(self.config['token'])
    async def on_ready(self):
        print(f"Logged in as {self.user}")
    async def on_message(self,message):
        if message.author == self.user:
            return
        for command in self.commands:
            if message.content.startswith(self.config['prefix']+command.name.lower()):
                await command.run(message,message.content.split(" ")[1:])
                return
            for alias in command.aliases:
                if message.content.startswith(self.config['prefix']+alias.lower()):
                    await command.run(message,message.content.split(" ")[1:])
                    return
bot = Battlecord("config.json",rawCommands)
