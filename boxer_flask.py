from flask import Flask, request, json, render_template, url_for, redirect, session
app= Flask(__name__)

## import json files

def getJSON(fileAndPathName):
	with open(fileAndPathName, 'r') as fp:
		return json.load(fp)
boxers = getJSON('./static/js/boxer.json')
joshua_ops = getJSON('./static/js/joshua.json')
wilder_ops = getJSON('./static/js/wilder.json')
breazeale_ops = getJSON('./static/js/breazeale.json')
duhaupas_ops = getJSON('./static/js/duhaupas.json')
fury_ops = getJSON('./static/js/fury.json')
klitschko_ops = getJSON('./static/js/klitschko.json')
martin_ops = getJSON('./static/js/martin.json')
molina_ops = getJSON('./static/js/molina.json')
ortiz_ops = getJSON('./static/js/ortiz.json')
parker_ops = getJSON('./static/js/parker.json')
povetkin_ops = getJSON('./static/js/povetkin.json')
takam_ops = getJSON('./static/js/takam.json')
whyte_ops = getJSON('./static/js/fury.json')
miller_ops = getJSON('./static/js/miller.json')

##search bar
def search_bar():
			for boxer in boxers:
				s=" "
				name=(boxer['fname'], boxer['lname'])
				search = request.form['search']
				if boxer['lname'] == search.capitalize():
					return redirect("/"+ boxer['lname'])
				elif boxer['alias'] == search.title() or boxer['alias'] == search:
					return redirect("/"+ boxer['lname'])
				elif (s.join(name)) == search.title():
					return redirect("/"+ boxer['lname'])
				elif boxer['fname'] == search.capitalize():
					return redirect("/"+ boxer['lname'])
##had to use another for, if statement because the else statement didn't work properly in loop and returned inacurate results
			for boxer in boxers:
				search = request.form['search']
				if boxer['lname'] != search.capitalize() or boxer['alias'] != search.title():
					return render_template('alert.html')

##app index
@app.route('/', methods=['GET','POST'])
def index():
	if request.method=='POST':
		return search_bar()
	return render_template('loop.html', boxers=boxers)
#sort by kos
@app.route('/byko', methods=['GET','POST'])
def kos():
	sorted_boxers=sorted(boxers, key=lambda d:d["kos"], reverse=True)
	if request.method=='POST':
		return search_bar()
	return render_template('loop.html', boxers=sorted_boxers)

#sort by position in world
@app.route('/world', methods=['GET','POST'])
def world():
	sorted_world=sorted(boxers, key=lambda d:d["Pos_in_w"])
	if request.method=='POST':
		return search_bar()
	return render_template('loop.html', boxers=sorted_world)

#sort by BoxRec rating
@app.route('/rating', methods=['GET','POST'])
def rating():
	sorted_rating=sorted(boxers, key=lambda d:d["rating"], reverse=True)
	if request.method=='POST':
		return search_bar()
	return render_template('loop.html', boxers=sorted_rating)
#sort by stance
@app.route('/Orthodox', methods=['GET','POST'])
def ortho():
	if request.method=='POST':
		return search_bar()
	ortho_boxers=[]
	for boxer in boxers:
		if boxer['stance'] == 'Orthodox':
			ortho_boxers.append(boxer)
	return render_template('loop.html', boxers=ortho_boxers)

@app.route('/Southpaw', methods=['GET','POST'])
def southp():
	if request.method=='POST':
		return search_bar()
	southp_boxers=[]
	for boxer in boxers:
		if boxer['stance'] == 'Southpaw':
			southp_boxers.append(boxer)
	return render_template('loop.html', boxers=southp_boxers)

#sort by british boxers
@app.route('/British', methods=['GET','POST'])
def british():
	if request.method=='POST':
		return search_bar()
	british_boxers=[]
	for boxer in boxers:
		if boxer['Nationality'] == 'British':
			british_boxers.append(boxer)
		sorted_b_boxers=sorted(british_boxers, key=lambda d:d["Pos_in_c"])
	return render_template('loop.html', boxers=sorted_b_boxers)
#sort by american boxers
@app.route('/American', methods=['GET','POST'])
def american():
	if request.method=='POST':
		return search_bar()
	american_boxers=[]
	for boxer in boxers:
		if boxer['Nationality'] == 'American':
			american_boxers.append(boxer)
		sorted_a_boxers=sorted(american_boxers, key=lambda d:d["Pos_in_c"])
	return render_template('loop.html', boxers=sorted_a_boxers)
#sort by french boxers
@app.route('/French', methods=['GET','POST'])
def french():
	if request.method=='POST':
		return search_bar()
	french_boxers=[]
	for boxer in boxers:
		if boxer['Nationality'] == 'French':
			french_boxers.append(boxer)
	return render_template('loop.html', boxers=french_boxers)
#sort by height
@app.route('/height', methods=['GET','POST'])
def height():
	if request.method=='POST':
		return search_bar()
	sorted_height=sorted(boxers, key=lambda d:d["height"], reverse=True)
	return render_template('loop.html', boxers=sorted_height)
#sort by age
@app.route('/age', methods=['GET','POST'])
def age():
	if request.method=='POST':
		return search_bar()
	sorted_age=sorted(boxers, key=lambda d:d["age"], reverse=True)
	return render_template('loop.html', boxers=sorted_age)
#sort by reach
@app.route('/reach', methods=['GET','POST'])
def reach():
	if request.method=='POST':
		return search_bar()
	sorted_reach=sorted(boxers, key=lambda d:d["reach"], reverse=True)
	return render_template('loop.html', boxers=sorted_reach)
#go to boxer info page with picture
@app.route('/<name>',methods=['GET', 'POST'])
def boxer_details(name=None):
	if request.method=='POST':
		return search_bar()
	return render_template('boxer_layout.html', boxers=boxers, name=name)
#further info pages for boxers:
@app.route('/Joshua/info', methods=['GET','POST'])
def joshua():
	if request.method=='POST':
		return search_bar()
	return render_template('Joshua.html')

@app.route('/Wilder/info', methods=['GET','POST'])
def wilder():
	if request.method=='POST':
		return search_bar()
	return render_template('Wilder.html')

@app.route('/Takam/info', methods=['GET','POST'])
def takam():
	if request.method=='POST':
		return search_bar()
	return render_template('Takam.html')

@app.route('/Povetkin/info', methods=['GET','POST'])
def povetkin():
	if request.method=='POST':
		return search_bar()
	return render_template('Povetkin.html')

@app.route('/Klitschko/info', methods=['GET','POST'])
def klitschko():
	if request.method=='POST':
		return search_bar()
	return render_template('Klitschko.html')

@app.route('/Parker/info', methods=['GET','POST'])
def parker():
	if request.method=='POST':
		return search_bar()
	return render_template('Parker.html')

@app.route('/Fury/info', methods=['GET','POST'])
def fury():
	if request.method=='POST':
		return search_bar()
	return render_template('Fury.html')

@app.route('/Breazeale/info', methods=['GET','POST'])
def breazeale():
	if request.method=='POST':
		return search_bar()
	return render_template('Breazeale.html')

@app.route('/Molina/info', methods=['GET','POST'])
def molina():
	if request.method=='POST':
		return search_bar()
	return render_template('Molina.html')

@app.route('/Whyte/info', methods=['GET','POST'])
def whyte():
	return render_template('Whyte.html')

@app.route('/Martin/info', methods=['GET','POST'])
def martin():
	if request.method=='POST':
		return search_bar()
	return render_template('Martin.html')

@app.route('/Duhaupas/info', methods=['GET','POST'])
def duhaupas():
	if request.method=='POST':
		return search_bar()
	return render_template('Duhaupas.html')

@app.route('/Miller/info', methods=['GET','POST'])
def miller():
	if request.method=='POST':
		return search_bar()
	return render_template('Miller.html')

@app.route('/Ortiz/info', methods=['GET','POST'])
def ortiz():
	if request.method=='POST':
		return search_bar()
	return render_template('Ortiz.html')

## recent fights for each boxer
@app.route('/Joshua/info/fights', methods=['GET','POST'])
def joshua_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=joshua_ops)

@app.route('/Wilder/info/fights', methods=['GET','POST'])
def wilder_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=wilder_ops)

@app.route('/Breazeale/info/fights', methods=['GET','POST'])
def breazeale_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=breazeale_ops,)

@app.route('/Duhaupas/info/fights', methods=['GET','POST'])
def duhaupas_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=duhaupas_ops)

@app.route('/Fury/info/fights', methods=['GET','POST'])
def fury_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=fury_ops)

@app.route('/Klitschko/info/fights', methods=['GET','POST'])
def klitschko_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=klitschko_ops)

@app.route('/Martin/info/fights', methods=['GET','POST'])
def martin_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=martin_ops)

@app.route('/Molina/info/fights', methods=['GET','POST'])
def molina_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=molina_ops)

@app.route('/Ortiz/info/fights', methods=['GET','POST'])
def ortiz_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=ortiz_ops)

@app.route('/Parker/info/fights', methods=['GET','POST'])
def parker_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=parker_ops)

@app.route('/Povetkin/info/fights', methods=['GET','POST'])
def povetkin_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=povetkin_ops)

@app.route('/Takam/info/fights',methods=['GET','POST'])
def takam_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=takam_ops)

@app.route('/Miller/info/fights',methods=['GET','POST'])
def miller_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=miller_ops)

@app.route('/Whyte/info/fights',methods=['GET','POST'])
def whyte_fights():
	if request.method=='POST':
		return search_bar()
	return render_template('opponent_layout.html', opponents=whyte_ops)

@app.errorhandler(404)
def page_not_found(error):
	return "The page requested cannot be found, make sure you have the correct URL."

@app.errorhandler(500)
def server_error(error):
	return "There is a problem with connection to the server. Please check connection to server, or contact server administrator."

@app.errorhandler(503)
def server_down(error):
	return "There is a problem with the server. Please try again in a few minutes or contact server administrator."

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
