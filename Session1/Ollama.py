import ollama

prompt = input("Enter your prompt: ")
response = ollama.generate(
    model="llama3.2",
    prompt=f"generate answer in 5 tokens only\n\nPrompt= {prompt}"
)
print(response["response"])