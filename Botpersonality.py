#import region
#For generating randomised out put from a list of values for a key in dictionaries of responses
import random

#define variables
name = "echo bot"

#variables
bot_Template = "Bot Says: {0}"
user_Template = "User Says {0}"

#sample responses
responses = {"How are you": [" Iam good, How about you", "Good , How are you", "Whats up, iam great, hope you are also doing good"], "Who are you": ["Iam your personel assistant {}".format(name), "Iam your personalised bot {}".format(name)]}

# methods
def respond(message):
    #choice method helps in picking random choice from the responce value for a key
    print(random.choice(responses[message]))


def default(message):
    if message.upper() == "BYE":
        print(bot_Template.format(" Bye"))
        exit()
    else:
        print(bot_Template .format(" not able to undetstand, can you please explain more"))
        return


while True:
    message = input(user_Template.format(""))
    if message in responses:
        respond(message)
    else:
        default(message)



