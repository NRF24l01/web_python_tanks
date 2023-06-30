from flask import Flask, render_template, jsonify
from helpers import generate_field, check_field, print_field
from config import host, port


app = Flask(__name__)

# Загружаем ваш массив из API
def load_array_from_api():
    # Здесь должен быть ваш код для получения массива с сервера по API
    # Возвращаем заглушку для примера
    field = generate_field(2, 10, 10 ,10)
    res = check_field(field)
    print_field(res[1])
    print(res[0])
    return res[1]

# Здесь должна быть логика для получения начального состояния игры
# Например, можно определить функцию get_initial_game_state() и вызвать её внутри /state
def get_initial_game_state():
    return [
        ['#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#'],
        ['#', '.', '@', '.', '#'],
        ['#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#']
    ]

# Обработка запроса на получение состояния игры
@app.route('/state', methods=['GET'])
def get_game_state():
    # Здесь должна быть логика для получения текущего состояния игры
    # Например, можно определить функцию get_current_game_state() и вызвать её вместо get_initial_game_state()
    current_state = get_initial_game_state()

    # Возвращаем состояние игры в формате JSON
    return jsonify(current_state)

# Генерируем HTML-страницу с помощью шаблона
@app.route('/')
def index():
    # array = load_array_from_api()
    # rows = len(array)
    # cols = len(array[0])
    return render_template('index.html')

# API endpoint для получения обновленного массива
@app.route('/api/array')
def get_array():
    array = load_array_from_api()
    return jsonify(array=array)

if __name__ == '__main__':
    app.run(debug=True, port=port, host=host)