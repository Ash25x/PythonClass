from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile.html")
def profile():
    return render_template("profile.html")

@app.route("/annoying.html")
def annoying():
    return render_template("annoying.html")

if __name__ == "__main__":
    app.run(debug=True)
