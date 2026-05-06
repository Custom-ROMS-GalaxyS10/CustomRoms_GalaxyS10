from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

ROM_FOLDER = "roms"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/roms")
def roms():
    data = {}

    for device in os.listdir(ROM_FOLDER):
        path = os.path.join(ROM_FOLDER, device)

        if os.path.isdir(path):
            files = os.listdir(path)

            # tylko zip / rar
            rom_files = [f for f in files if f.endswith(".zip") or f.endswith(".rar")]

            data[device] = rom_files

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)