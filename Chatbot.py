def chatbot_answer(user_input):
    user_input = user_input.lower()

    if "hey there" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how's your day" in user_input:
        return "I'm here to help, and it's a good day when I can assist you. What can I do for you?"

    elif "what's your role?" in user_input or "who are you?" in user_input:
        return "I am Deepa, your helpful virtual assistant."

    elif "tell me a joke" in user_input:
        return "Why did the computer keep freezing? Because it left its Windows open!"

    elif "share an interesting fact" in user_input:
        return "Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."

    elif "recommend a movie" in user_input:
        return "I recommend watching 'The Shawshank Redemption.' It's a classic that many people love."
    elif "bye"  in user_input or "goodbye" in user_input:
        return "Goodbye! If you ever want to talk again, feel free to start a new conversation."

    else:
        return "I'm sorry, I don't have an answer for that question. Can you please rephrase or ask something else?"

def main():
    bot_name = "Deepa"
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print(f"{bot_name}: Bye! It was nice talking you!.")
            break
        else:
            response = chatbot_answer(user_input)
            print(f"{bot_name}:", response)

if __name__ == "__main__":
    main()

