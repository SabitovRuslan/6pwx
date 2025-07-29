from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "name": "Ruslan Sabitov",
        "nick": "6pwx",
        "contacts": [
            {"name": "Telegram", "url": "https://t.me"},
            {"name": "Github", "url": "https://github.com/SabitovRuslan"},
            {"name": "Discord", "url": "https://google.com"},
            {"name": "Codeforces", "url": "https://codeforces.com/"}
        ],
        "hobbies": [
            "sport programming(cpp)",
            "CTF enjoyer",
            "ml(python, a little)",
            "math"
        ],
        "location": "Russia, Saint-Petersburg"
    }

    return render_template("index.html", **data)

if __name__ == "__main__":
    app.run(debug=True)