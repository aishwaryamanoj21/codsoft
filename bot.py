import re

def chat_with_bot(user_input):
    # Predefined responses
    responses = {
        "greeting": "Hello! How can I help you today?",
        "farewell": "Goodbye! Have a great day!",
        "name": "I'm a chatbot created to assist you.",
        "default":"I ll find out the best suggestion for you." 
    }
    
    # Patterns for matching user input
    patterns = {
        "greeting": re.compile(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", re.IGNORECASE),
        "farewell": re.compile(r"\b(goodbye|bye|see you|farewell)\b", re.IGNORECASE),
        "name": re.compile(r"\b(your name|who are you)\b", re.IGNORECASE)
    }

    # Check user input against patterns
    for key, pattern in patterns.items():
        if pattern.search(user_input):
            return responses[key]

    # Default response if no patterns matched
    return responses["default"]

# Example usage
user_queries = [
    "Hello!",
    "What's your name?",
    "Where can i get best icecream?.",
]

for query in user_queries:
    print(f"User: {query}")
    print(f"Bot: {chat_with_bot(query)}")
