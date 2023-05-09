import openai

openai.api_key = "your_api_key_here"

# Define function to get AI response to a question
def QuestionsAnswer(question, chat_log=None):
    
    # Load chat log from file
    with open("Data/qna_log.txt", "r") as f:
        chat_log_template = f.read()

    # Use chat_log_template if chat_log is not provided
    if chat_log is None:
        chat_log = chat_log_template

    # Define prompt
    prompt = f'{chat_log}Question: {question}\nAnswer:'

    # Send prompt to OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Get answer from response
    answer = response.choices[0].text.strip()

    # Update chat log file
    chat_log_template_update = chat_log_template + f"\nQuestion: {question}\nAnswer: {answer}"
    with open("Data/qna_log.txt", "w") as f:
        f.write(chat_log_template_update)

    # Return answer
    return answer