from flask import Flask, jsonify, request
import sqlite3
import requests

people_search_app = Flask(__name__)

def initialization():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        birth_date TEXT NOT NULL
        );'''
    )
    conn.commit()
    conn.close()

def insertion(user):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT id FROM user WHERE first_name=? AND last_name=?", (user['fname'], user['lname']))
    existing_user = c.fetchone()

    if existing_user:
        print(f"User with first_name '{user['fname']}' and last_name '{user['lname']}' already exists. Skipping insertion.")
    else:
        query = f"INSERT INTO user (first_name, last_name, age, gender, email, phone, birth_date) VALUES ('{user['fname']}', '{user['lname']}', {user['age']}, '{user['gender']}', '{user['email']}', '{user['phone']}', '{user['bdate']}');"
        c.execute(query)
        print('\nSuccessfully Inserted...\n')
    
    conn.commit()
    conn.close()

def search_fname(fname):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM user WHERE first_name LIKE '%"+fname+"%';"
    cursor.execute(query)
    all_rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return all_rows

@people_search_app.route("/")
def Home():
    return jsonify({"message":"Welcome to the Home page of People Search Api , begins its uses by going to http://127.0.0.1:5000/api/users?first_name=."})

@people_search_app.route("/api")
def Api():
    return jsonify({"message":"Welcome to the API page of People Search Api , begins its uses by going to http://127.0.0.1:5000/api/users?first_name=."})


@people_search_app.route("/api/users")
def get_users():
    dummy_users=[]
    first_name = request.args.get("first_name")
    if not first_name:
        return jsonify({"message":"error","error": "Please provide the first_name parameter as http://127.0.0.1:5000/api/users?first_name=."}), 400

    users = search_fname(first_name)
    if users:
        return jsonify({"message":"local database fetching","users": users})
    else:
        dummyjson_url = f"https://dummyjson.com/users/search?q={first_name}"
        response = requests.get(dummyjson_url)
        if response.status_code == 200:
            dummyjson_users = response.json()['users']
            user = {}
            for i in range(len(dummyjson_users)):
                user['fname'] = dummyjson_users[i]['firstName']
                user['lname'] = dummyjson_users[i]['lastName']
                user['age'] = dummyjson_users[i]['age']
                user['gender'] = dummyjson_users[i]['gender']
                user['email'] = dummyjson_users[i]['email']
                user['phone'] = dummyjson_users[i]['phone']
                user['bdate'] = dummyjson_users[i]['birthDate']
                dummy_users.append(user)
                user = {}

            for i in range(len(dummy_users)):
                insertion(dummy_users[i])
            return jsonify({"message":"online dummyjson api fetching","users": dummy_users})

    return jsonify({"error": "Error fetching users from the dummyjson API."}), 500

print("App Executed successfully.")

if __name__ == "__main__":
    people_search_app.run()