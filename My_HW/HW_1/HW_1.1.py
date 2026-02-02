from flask import Flask




app = Flask(__name__)

@app.route("/")   # Название главной страницы начинается с символа "/", его отсутствие и било проблемой
def home():
    return"Hello, World!"


if __name__=="__main__":

    app.run()