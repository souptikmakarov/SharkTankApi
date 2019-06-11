from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
from flask_cors import CORS, cross_origin
from GroupByCat2 import GroupBy, GetUserInfo

app = Flask('myApi')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# users = ["Abhimanyu_Yadav","Adarsh_Thompson","Ajit_Menon","Bhaskar_Ghatak","Dinesh_C","Jubi_jose_Jose","Mohit_Panwar","Nishant_Kumar3","Nisha_Handa","Sabarinath_B","Sachin_Juneja","Smitha_Karthik","Vamsi_V_Krishna","Veena_Chandrashekhar","Zeeshan_Faisal"]
users = ["Bhaskar_Ghatak","Dinesh_C","Mohit_Panwar"]

def PlotUserData(data, name, type, value):
	category = list(map(lambda x: data[x]['Type'], data))
	hours = list(map(lambda x: data[x]['Duration'], data))

	fig1, ax1 = plt.subplots()
	ax1.pie(hours, labels=category, autopct='%1.1f%%', shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	fileName = 'C:\My_Files\Projects\SharkTank\DemoApp\TimeWisePlots\{}-{}-{}.png'.format(name, type, value)
	fig1.savefig(fileName)
	return fileName

@app.route('/')
def fy():
	return 'Server is up'

@app.route('/getAvailableUsers')
@cross_origin()
def GetAvailableUsers():
	return jsonify({"Users": users})

@app.route('/getUserDataRange')
@cross_origin()
def GetUserDataRange():
	name = request.args['name']
	return jsonify(GetUserInfo(name))


# @app.route('/getUserDataPlot')
# @cross_origin()
# def GetUserData():
# 	name = request.args['name']
# 	if name in users:
# 		for userData in categoryData:
# 			if userData['User'] == name:
# 				return PlotUserData(userData['CatData'], name)
	# return plotfile

@app.route('/getTimeUserDataPlot')
@cross_origin()
def GetUserDataPlot():
	name = request.args['name']
	type = request.args['type']
	value = request.args['value']
	if name in users:
		userData = GroupBy(type, value, name)
		return jsonify({
			"imageLocation": PlotUserData(userData['CatData'], name, type, value),
			"isDataValid": userData["isDataValid"]
		})

@app.route('/getTimeUserData')
@cross_origin()
def GetUserData():
	name = request.args['name']
	type = request.args['type']
	value = request.args['value']
	mock = True if request.args['mock'] == "true" else False
	print(mock)
	if name in users:
		userData = GroupBy(type, value, name, mock)
		return jsonify(userData)

if __name__ == '__main__':
	app.run(debug=True)