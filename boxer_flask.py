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

@app.route('/aj')
def aj():
	return render_template('aj.html', boxers=boxers)



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

