import discord
class Command():
    def __init__(self, bot):
        self.bot = bot
        self.name = "Help"
        self.description = "Shows this message."
        self.usage = "help"
        self.aliases = ["h", "commands"]
        self.category = "General"
        self.usage = "help"
        
    async def run(self, message, args):
        embed = discord.Embed(title="Battlecord Help", description="Here is a list of all the commands.", color=0x00ff00)
        for command in self.bot.commands:
            # we want to put all the command info in the embed
            value = f"**Description:** {command.description}\n**Usage:** {command.usage}\n**Aliases:** {', '.join(command.aliases)}\n**Category:** {command.category}"
            embed.add_field(name=command.name, value=value, inline=False)
        await message.channel.send(embed=embed)
main = Command