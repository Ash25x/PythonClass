from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(name):
    return render_template('index.html', user = name)

if __name__=="__main__":
    app.run()
