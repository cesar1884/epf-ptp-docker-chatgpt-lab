from flask import Flask,request
import os
import openai

app = Flask(__name__)
#e
openai.api_key = os.environ.get('OPENAI_KEY')


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/chatgpt')
def chatgpt():
    args = request.args
    message =args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

@app.route('/codegen', methods=['POST'])
def generate_code():
    data = request.get_json()
    language = data['language']
    content = data['content']
    completion = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Generate code in {language} programming language: {content}",
        temperature=0.5,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion['choices'][0]['text']
