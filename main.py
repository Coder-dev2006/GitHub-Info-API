from flask import Flask, jsonify
import requests

app = Flask(__name__)

# GitHub foydalanuvchi nomini shu yerda yoz
GITHUB_USERNAME = "Coder-dev2006"

@app.route('/')
def home():
    return jsonify({"message": "Welcome to GitHub Info API", "creator": "Fayziyev Samandar"})

@app.route('/profile')
def get_profile():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}"
    response = requests.get(url)
    data = response.json()

    profile_data = {
        "username": data.get("login"),
        "name": data.get("name"),
        "bio": data.get("bio"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "github_url": data.get("html_url")
    }

    return jsonify(profile_data)

if __name__ == "__main__":
    app.run(debug=True)
