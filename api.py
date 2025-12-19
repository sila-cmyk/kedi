from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Docker Kedi API Çalışıyor 🐱"})

@app.route("/kedi")
def kedi():
    r = requests.get("https://catfact.ninja/fact")
    data = r.json()
    return jsonify({
        "kedi_bilgisi": data["fact"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
