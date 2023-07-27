import random
import re

def generate_random_response():
    greetings = [
        "Hello!", "Hi!", "Hey!", "Greetings!",
        "Hi there!", "Hello there!", "Hey, how's it going?",
        "Hey, nice to meet you!", "Hi, what can I do for you?", "Hello, how can I assist you today?",
        "Hi, how are you doing?", "Hello, what's up?", "Hi there, how may I help you?",
        "Hey, it's good to see you!", "Hello, what brings you here?",
        "Hi, what's happening?", "Hello, how's your day going?",
        "Hi, nice to have you here!", "Greetings and salutations!", "Hi there, what's on your mind?",
        "Hello, how can I make your day better?", "Hi, how's everything with you?",
        "Hello, what can I do to brighten your day?"
    ]
    how_are_you = [
        "I'm just your friendly chat friend, but thanks for asking!", "I'm doing fine!",
        "I'm here to assist you!", "I'm good, thank you!", "I'm ready to help!",
        "I'm just a program, so I don't have feelings.",
        "I'm doing well, and you?", "I'm functioning properly, thanks for asking!",
        "I'm great, thanks!", "I'm always here, ready to chat!",
        "I'm alive and ready to chat!", "I'm doing well, thank you for asking.",
        "I'm doing splendidly!", "I'm feeling excellent!", "I'm doing quite well, how about you?",
        "I'm doing just fine, thanks for checking!", "I'm here, ready to assist you 24/7!"
    ]
    bot_name = [
        "You can call me your friendly chat friend.", "Feel free to refer to me as your buddy.",
        "I'm your helpful chat companion.",
        "You can call me your chatty pal.",
        "I'm just here to be your friendly conversational partner.",
        "I'm your virtual friend here to chat.",
        "I'm your trusty companion in conversations.",
        "You can call me your talkative buddy.", 
        "You can address me as your friendly chat helper.",
        "I'm here to be your helpful chat friend.", 
        "I'm just your chat companion, always here for you."
    ]
    goodbyes = [
        "Goodbye!", "Farewell!", "Take care!", 
        "Goodbye! Have a great day!",
        "Until next time!", "See you later!", 
        "Goodbye, have a nice day!",
        "Goodbye, it was nice talking to you!",
        "Goodbye, take care and stay safe!",
        "Goodbye, see you soon!", 
        "Farewell, have a wonderful day!",
        "Goodbye, feel free to return anytime!", 
        "Goodbye, stay happy and healthy!",
        "Farewell, my friend!",
        "Take care and have a splendid day!",
        "Goodbye, till we meet again!",
        "Goodbye, have a fantastic time ahead!", 
        "Until we chat again, goodbye!",
        "Farewell, and remember,
        I'm always here when you need me!"
    ]
    default_response = [
        "I'm not sure how to respond to that. Can you be more specific?", "I didn't quite get that.",
        "I'm still learning, and I'm not sure how to answer that.",
        "Can you rephrase your question?", "I'm sorry, could you please repeat that?",
        "I'm not programmed to understand that query.", "I'm still learning new things!",
        "My apologies, I'm not familiar with that topic.", "Hmm, let me think about that.",
        "I'm constantly learning, and I appreciate your input!",
        "I'm afraid I don't have the answer to that right now.",
        "I'm a language model, not an encyclopedia, but I'll do my best!",
        "I wish I could help you with that, but I'm limited in my capabilities.",
        "I'm just a program, so I can't comprehend everything.",
        "I'm here to chat, but I might not have all the answers.",
        "I'm not omniscient, but I'll try my best to assist you.",
        "I'm just here to be your chatty companion.",
        "I'm just a chat friend, not a human, so my understanding is limited.",
        "I'm an AI, but I still have my limitations.",
        "I'm just a friendly chat friend, not a human expert, so I may not know everything.",
        "I'm still learning, so bear with me!", "My knowledge is expanding every day!",
        "I'm constantly being updated with new information.",
        "I'm always striving to improve and provide better responses."
    ]

    all_responses = greetings + how_are_you + bot_name + goodbyes + default_response

    return random.choice(all_responses)
