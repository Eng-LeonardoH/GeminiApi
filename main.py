import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown

import google.generativeai as genai

def to_markdown(text):
  text = text.replace('*', '')
  return Markdown(textwrap.indent(text, "" ,predicate=lambda _: True))

genai.configure(api_key="AIzaSyBndBpTLOrKNziUW6fXYTMr85QrhmHvKXE")
generationConfig = {
    "candidate_count": 1,
    "temperature": 1,
}
safetySettings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}
modelName = "gemini-1.0-pro"
model = genai.GenerativeModel(model_name = modelName, generation_config = generationConfig, safety_settings = safetySettings)

print(model.generate_content("Olá, quem é você ?").text)

chat = model.start_chat(history=[])
print("Novo chat inicializado...")
while True:
    prompt = input("Esperando a próxima entrada: ")
    if prompt == "sair":
        break
    response = chat.send_message(prompt)
    print(modelName, ":\n", to_markdown(response.text).data)