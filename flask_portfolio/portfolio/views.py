## FROM THE CURRENT DIRECTORY, IMPORT APP
from . import app
from flask import render_template, request
## CREATE AN INDEX ROUTE AND A FUNCTION(PAGE) FOR IT

comments = [{'name' :'Ash','message' : 'Dont like you'},
			{'name': 'Saroosh', 'message': 'bring me a beer, Please!'}]


@app.route('/')
def index():
    print('it\'s running')
    return render_template('/index.html')

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
	if request.method == 'POST':
		name1 = request.form['name']
		message1 = request.form['message'] 
		comments.append({'name' : name1, 'message': message1})

		print(comments)
		return render_template('/info.html', messages = comments)
	else:
		print('get method')
		print(comments)
		return render_template('info.html', messages= comments)
