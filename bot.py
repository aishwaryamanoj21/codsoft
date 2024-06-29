import re

def chat_with_bot(user_input):
    responses = {
        "greeting": "Hello! How can I help you today?",
        "farewell": "Goodbye! Have a great day!",
        "name": "I'm a chatbot created to assist you.",
        "default":"I ll find out the best suggestion for you." 
    }
    
    patterns = {
        "greeting": re.compile(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", re.IGNORECASE),
        "farewell": re.compile(r"\b(goodbye|bye|see you|farewell)\b", re.IGNORECASE),
        "name": re.compile(r"\b(your name|who are you)\b", re.IGNORECASE)
    }

    for key, pattern in patterns.items():
        if pattern.search(user_input):
            return responses[key]


    return responses["default"]


user_queries = [
    "Hello!",
    "What's your name?",
    "Where can i get best icecream?.",
]

for query in user_queries:
    print(f"User: {query}")
    print(f"Bot: {chat_with_bot(query)}")
