from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
    return "<h1>My choice Online Store</h1>"

@app.route("/about")
def about_view():
    return "<h2>This is the about page</h2>"

if __name__ == "__main__":
    app.run()