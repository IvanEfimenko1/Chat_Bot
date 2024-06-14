from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

app = Flask(__name__)

# Load the tokenizer and model
local_model_path = '/app/model'  # Указываем путь к модели внутри контейнера
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForCausalLM.from_pretrained(local_model_path)

# Create a text generation pipeline
generator = pipeline(
    'text-generation', 
    model=model, 
    tokenizer=tokenizer, 
    device=0 if torch.cuda.is_available() else -1
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    generated_texts = generator(
        question, 
        max_length=100, 
        num_return_sequences=1, 
        temperature=0.1,
        top_p=0.92,
        top_k=50,
        truncation=True
    )
    answer = generated_texts[0]['generated_text']
    # Формируем HTML ссылку
    answer = answer.replace("https://example.com/data-pipeline", '<a href="https://example.com/data-pipeline">https://example.com/data-pipeline</a>')
    return render_template('index.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
