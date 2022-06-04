from flask import Flask, jsonify, request
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

CORS(app)


async def translate(text, target):
    translator = Translator()
    translation = translator.translate(text, dest=target)
    return translation.text


@app.route("/")
async def get_data():
    text = request.args.get("q")
    if text is None:
        return jsonify({"error": "Parameter 'q' is missing"}), 400

    data = {
        "error": "",
        "data": {
            "text": text,
            "result": await translate(text, "id")
        }
    }
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)
