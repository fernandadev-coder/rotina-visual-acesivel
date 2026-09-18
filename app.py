from flask import Flask, render_template

app = Flask(__name__)

ATIVIDADES_PADRAO = [
    {"id": 1, "nome": "Acordar", "icone": "☀️"},
    {"id": 2, "nome": "Escovar os Dentes", "icone": "🪥"},
    {"id": 3, "nome": "Tomar Café", "icone": "🥛"},
    {"id": 4, "nome": "Ir para a Escola", "icone": "🎒"},
    {"id": 5, "nome": "Terapia", "icone": "🧩"},
    {"id": 6, "nome": "Almoçar", "icone": "🍽️"},
    {"id": 7, "nome": "Brincar / Descanso", "icone": "🧸"},
    {"id": 8, "nome": "Tomar Banho", "icone": "🛁"},
    {"id": 9, "nome": "Jantar", "icone": "🍲"},
    {"id": 10, "nome": "Dormir", "icone": "🌙"},
]

@app.route("/")
def index():
    return render_template("index.html", atividades=ATIVIDADES_PADRAO)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)