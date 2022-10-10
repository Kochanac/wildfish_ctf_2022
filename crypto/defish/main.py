from flask import Flask, render_template, request
from fish import fishify

app = Flask(__name__)

@app.route('/')
def index():
    text = request.args.get("eng_text")
    fish_text = fishify(text)

    return render_template("index.html", text=(text or ""), fish_text=fish_text)



if __name__ == "__main__":
    app.run("0.0.0.0", port=8080)