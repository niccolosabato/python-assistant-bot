print("Welcome to fAssistant!!!!!!!!!")
print("I can help you with something stupid...")

while True:
    print('Type what you want or "help" for the commands list:')
    request=input()

    import time

    if request == "help":
        print("Commands list:\n1. help \n2. exit\n3. time \n4. date")

    if request == "time":
        print(time.strftime("%H.%M.%S"))

    if request == "date":
        print(time.strftime("%d.%m.%Y"))

    if request == "exit":
        exit()   
