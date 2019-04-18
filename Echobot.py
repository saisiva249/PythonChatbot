bot_Template = "Bot Says: "
user_Template = "User Says"
import  time

while True:
    message = input(user_Template + "")
    if message.upper() == "BYE":
        time.sleep(2)
        print(bot_Template + " Bye")
        break
    else:
        time.sleep(2)
        print(bot_Template + " i am hearing that you said " + message)
