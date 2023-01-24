import openai

# Add your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

generated_text = generate_text("Write a short story about a robot who wants to be human")
print(generated_text)