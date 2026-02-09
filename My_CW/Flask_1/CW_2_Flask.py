from flask import Flask


app = Flask(__name__)  # __main__ | app.py

# 1. host == localhost:5000
# localhost == 127.0.0.1
# 2. /
@app.route("/")
def index():
    return "<h1>Hello from our first application!</h1>"


@app.route("/username/<username>")
def greetings(username):
    return f"Greetings, {username}"


if __name__ == "__main__":
    app.run(debug=True)