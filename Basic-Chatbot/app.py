import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

def castle_swimmer_chatbot(user_input):
    tokens = word_tokenize(user_input.lower())  
    
    if "castle" in tokens:
        return "Castle Swimmer is a webtoon that explores themes of prophecy and the fates of its characters."
    elif "swimmer" in tokens:
        return "Castle Swimmer is a webtoon that explores themes of prophecy and the fates of its characters."
    elif "characters" in tokens:
        return "The main characters include Siren, a prince, and Kappa, the beacon of prophecy."
    elif "prophecy" in tokens:
        return "The prophecy involves Kappa and Siren, revealing their destinies."
    elif "siren" in tokens:
        return "Siren is a prince from the shark kingdom, crucial to the unfolding events."
    elif "kappa" in tokens:
        return "Kappa is central to the webtoon's plot and serves as a beacon of prophecy."
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