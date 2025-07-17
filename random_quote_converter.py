import random

def get_random_quote():
    quotes = [
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "Your time is limited, don't waste it living someone else's life.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "The only way to do great work is to love what you do."
    ]
    return random.choice(quotes)

print(get_random_quote())
