from flask import Flask, render_template, request
app =Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    greeting = "Hello world"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name} "
        return render_template("index.html", greeting = greeting)
    else:
        return render_template("index.html")



# def p1():
#     name = 'Ash'
#     day = 'Tuesday'
#     return render_template('index.html', name= name, day = day)

if __name__=="__main__":
    app.run(debug=True)
