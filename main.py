print("Welcome to fAssistant")
print("I can help you with something stupid...")
print('Type what you want or "help" for the commands list:')

request=input()

import time

if request == "help":
    import help_menu

if request == "time":
    print(time.strftime("%H.%M.%S"))

if request == "date":
    print(time.strftime("%d.%m.%Y"))

