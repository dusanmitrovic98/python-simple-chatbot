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
