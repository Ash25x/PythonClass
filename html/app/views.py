from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
    return('Homepage')

@app.route('/2')
def second_page():
    return ('You are on 2nd page')

if __name__ == "__main__":
    app.run()
