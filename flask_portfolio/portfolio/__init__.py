from flask import Flask, render_template, request
app = Flask('portfolio')

from . import views



# if __name__ == "__main__":
#     app.run(debug=True)
