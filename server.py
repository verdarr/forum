from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Путь к файлу, в котором будут храниться сообщения
DATA_FILE = 'messages.txt'

# Функция для загрузки сообщений из файла
def load_messages():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Функция для сохранения сообщений в файл
def save_messages(messages):
    with open(DATA_FILE, 'w') as file:
        json.dump(messages, file)

# Главная страница, отображающая клиентскую часть
@app.route('/')
def index():
    return render_template('index.html')

# API для получения сообщений
@app.route('/api/messages', methods=['GET'])
def get_messages():
    messages = load_messages()
    return jsonify(messages)

# API для отправки и сохранения нового сообщения
@app.route('/api/messages', methods=['POST'])
def post_message():
    data = request.json
    messages = load_messages()
    messages.append(data)
    save_messages(messages)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)