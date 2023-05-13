import os, importlib
blacklist = ['classes.py', '__init__.py']
command_objects = []
for file in os.listdir('commands'):
    if file in blacklist:
        continue
    if not file.endswith('.py'):
        continue

    command = importlib.import_module(f'commands.{file[:-3]}')
    # get the class from the module, it should in a variable called 'main'
    command = command.main
    command_objects.append(command)