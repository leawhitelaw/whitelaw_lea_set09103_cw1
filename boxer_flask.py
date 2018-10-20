from flask import Flask, request, json, render_template, url_for
app= Flask(__name__)

## import json file

def getJSON(fileAndPathName):
	with open(fileAndPathName, 'r') as fp:
		return json.load(fp)
boxers = getJSON('./static/boxer.json')

##app index
@app.route('/')
def index():
	return render_template('loop.html', boxers=boxers)

@app.route('/<name>')
def boxer_details(name=None):
	return render_template('boxer_layout.html', boxers=boxers, name=name)

@app.route('/Joshua/info')
def joshua():
	return render_template('Joshua.html')
		
@app.route('/Wilder/info')
def wilder():
	return render_template('Wilder.html')

@app.route('/Takam/info')
def takam():
	return render_template('Takam.html')

@app.route('/Povetkin/info')
def povetkin():
	return render_template('Povetkin.html')

@app.route('/Klitschko/info')
def klitschko():
	return render_template('Klitschko.html')

@app.route('/Parker/info')
def parker():
	return render_template('Parker.html')	

@app.route('/Fury/info')
def fury():
	return render_template('Fury.html')

@app.route('/Breazeale/info')
def breazeale():
	return render_template('Breazeale.html')

@app.route('/Molina/info')
def molina():
	return render_template('Molina.html')

@app.route('/Whyte/info')
def whyte():
	return render_template('Whyte.html')

@app.route('/Martin/info')
def martin():
	return render_template('Martin.html')

@app.route('/Duhaupas/info')
def duhaupas():
	return render_template('Duhaupas.html')

@app.route('/Miller/info')
def miller():
	return render_template('Miller.html')

@app.route('/Ortiz/info')
def ortiz():
	return render_template('Ortiz.html')


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)


