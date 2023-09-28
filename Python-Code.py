import openai
import re

# set up OpenAI API key
openai.api_key = "..."

# define function to generate questions
def generate_questions(paragraph, num_questions=3):
    # split paragraph into sentences
    sentences = re.split('(?<=\w\.)\s', paragraph)

    # initialize list to store generated questions
    questions = []

    # loop through sentences and generate questions using ChatGPT
    for sentence in sentences:
        for i in range(num_questions):
            prompt = "Generate a question for this sentence: " + sentence
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=50,
                n=1,
                stop=None,
                temperature=0.5,
            )
            question = response.choices[0].text.strip()
            questions.append(question)

    # return list of generated questions
    return questions

# example usage
paragraph = "The key difference between a Docker image Vs a container is that a Docker image is a read-only immutable template that defines how a container will be realized. A Docker container is a runtime instance of a Docker image that gets created when the $ docker run command is implemented."
questions = generate_questions(paragraph, num_questions=5)
print(questions)
