import nltk

nltk.download('punkt')

def castle_swimmer_chatbot(user_input):
    user_input = user_input.lower()
    
    if "what is castle swimmer" in user_input:
        return "Castle Swimmer is a fantasy webtoon about a prophecy and the characters tied to it, exploring themes of destiny and love."
    elif "main characters" in user_input:
        return "The main characters are Kappa, the beacon of prophecy, and Siren, a prince tasked with fulfilling the prophecy."
    elif "prophecy" in user_input:
        return "The prophecy involves Kappa and Siren, with new revelations about their fates unfolding in chapters 83-89."
    elif "siren" in user_input:
        return "Siren is a prince from the shark kingdom, and he plays a crucial role in the prophecy."
    elif "kappa" in user_input:
        return "Kappa is the beacon of prophecy, destined to be a pivotal figure in Siren's journey."
    else:
        return "I'm not sure about that. Ask me about Castle Swimmer, its characters, or the prophecy!"

print("Bot: Hi! Ask me anything about Castle Swimmer.")
while True:
    user_question = input("You: ")
    if user_question.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break
    response = castle_swimmer_chatbot(user_question)
    print(f"Bot: {response}")
