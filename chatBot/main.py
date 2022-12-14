import random

# Creating greetings list
greetings = ["hi", "Hello", "What's up?!", "Howz you?", "Greetings!"]

# Creating goodbye list
goodbye = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]

keywords = ["up to", "ai", "ecc", "placements"]

response = ["preparing for entrance exams!", "AI is so exciting!", "ECC is so difficult", "Placements are coming soon!"]

print(random.choice(greetings))

user_response = ""

while user_response != "bye":
    user_response = input("Go ahead type something (or type bye to quit): ")
    user_response = user_response.lower().strip()
    if user_response == "bye":
        print(random.choice(goodbye))
        break
    is_key_found = False

    for index in range(len(keywords)):
        if keywords[index] in user_response:
            print("Rusty_The_Bot: ", response[index])
            is_key_found = True
        else:
            continue

    if not is_key_found:
        print("I am new to your world,I love learning new things!")
        keywords.append(user_response)
        # print(keywords)
        new_response = input("Tell me the correct response to " + user_response + " ? ")
        print("thank you for teaching me!!")
        response.append(new_response)
        # print(response)
