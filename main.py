print("Welcome to fAssistant")
print("I can just print the time and the date for now...")
print('Type "time" to print the time or "date" to print the date:')

request=input()
import time

if input=="date":
    print(time.strftime("%H.%M.%S"))
else:
    print(time.strftime("%d.%m.%Y"))

