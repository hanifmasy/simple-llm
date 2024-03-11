from langchain.output_parsers import ResponseSchema
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Define the response schema
response_schema = ResponseSchema(
    name="MovieResponse",
    description="The assistant's response about movies",
    fields=[
        {"name": "greeting", "type": "string", "description": "The assistant's greeting"},
        {"name": "question", "type": "string", "description": "The user's question about movies"},
        {"name": "answer", "type": "string", "description": "The assistant's answer to the user's question"},
    ]
)

# Create a prompt to request a conversation about movies
prompt = PromptTemplate(
    template="Assistant, {greeting}! The user has a question about movies: {question}\nAnswer: {answer}",
    input_variables=["greeting", "question", "answer"],
    partial_variables={"response_schema": response_schema}
)

# Define a query to prompt the model
query = {
    "greeting": "Hello!",
    "question": "What is your favorite movie?",
}

# Generate the output
output = model(prompt.format(**query))

# Parse the output using the response schema
parsed_result = response_schema.parse_json(output)

# Print the result
print(f"Assistant: {parsed_result['answer']}")
