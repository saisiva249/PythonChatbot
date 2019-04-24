import re

# ==============pattern matching ================
# consists of set of rules for matching user messages
# pattern matching this can be done using the regular expression
# '.' in regular expression matches any character
# '*' represents occurrence of one or more of the pattern specified before this


# we can search whether a message matches a pattern by using re.search(pattern, message)
# this returns a match object, if found else match  object is none

# adding parenthesis in a regular expression defines a group (.*)
# A group is just the substring that we are going to receive after matching the pattern
# we use the match object group method to retrieve the parts of the string that matched
# Default group with index 0 is the whole string
# the group with index 1 is the group we define by including the parenthesis in the pattern


# ==============Grammatical transformation================
# to make the response grammatically coherent we want to transform the extracted phases
# re.sub() helps in substituting patterns in a string

bot_response = "bot: "
user_response = "user: "


def get_response(inputresponse):
    responses = {"do you know", "Yes I Know"}
    if re.search(inputresponse, responses):
        return responses[inputresponse]
    else:
        return ""


def gram_change(inputtrans):
    re.sub('your', 'mine', inputtrans)


while True:
    message = input()
    pattern = 'do you know (.*)'

    match = re.search(pattern, message)
    if match:
        phrase = match.group(1)
        response = get_response(pattern)

        if response != '':
            print(response.format(gram_change(phrase)))
        else:
            print("can you please explain more")
