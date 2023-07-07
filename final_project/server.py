from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", static_folder="static")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    tt = translator.english_to_french(textToTranslate)
    return tt


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    tt = translator.french_to_english(textToTranslate)
    return tt


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
