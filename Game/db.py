import sqlite3

def create_db():
    conn = sqlite3.connect('database.sql')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS states (
    score INTEGER DEFAULT 0,
    coins INTEGER DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()

def update_score(score):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('database.sql')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO states (score) VALUES (?)', (score, ))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

def get_score():

    l = []

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('database.sql')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute('SELECT score FROM states')
    scores = cursor.fetchall()

    # Выводим результаты
    for score in scores:
        l.append(score)
    result = max(l)
    connection.close()
    return result

def update_coins(coins):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('database.sql')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO states (coins) VALUES (?)', (coins, ))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

def get_coins():

    result = []

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('database.sql')
    cursor = connection.cursor()

    # Выбираем всех пользователей
    cursor.execute('SELECT coins FROM states')
    coins = cursor.fetchall()

    # Выводим результаты
    for coin in coins:
        result.append(coin[0])

    connection.close()
    return max(result)