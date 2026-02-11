from flask import Flask




app = Flask(__name__)

@app.route("/")
def index():
    return "<h3>Hello, my first Flask!</h3>"


@app.route("/user/<name>")
def welcome(name):
    return f"<h1>Hello {name}, welcome my first Flask</h1>"


if __name__=="__main__":

    app.run(debug=True)
