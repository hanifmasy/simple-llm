from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Initialize the chatbot instance
chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Initialize an empty list to store the conversation history
messages = []

# Start a loop to interact with the chatbot
while True:
    # Get user input
    message = input("> ")
    # Create a HumanMessage object with the user's input
    usr_msg = HumanMessage(content=message)
    # Append the user's message to the conversation history
    messages.append(usr_msg)
    # Get the chatbot's response
    ai_msg = chat(messages)
    # Print the chatbot's response
    print(ai_msg.content)
    # Append the chatbot's response to the conversation history
    messages.append(ai_msg)
