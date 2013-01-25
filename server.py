from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/")
def homepage():
    return "Hello World!"


if __name__ == "__main__":
    app.run()