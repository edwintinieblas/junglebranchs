from configs import *

app = Flask(__name__)
#api = restful.Api(app)
api = Api(app)

@app.route("/")
def hello():
	return "\n|  |_______/)______/)_____\n|  |¯¯\)¯¯¯¯¯¯¯\)¯¯¯¯¯¯\)¯\n|  |\n|  |__API__JUNGLEBRANCHS__\n|  |\n|  |_______/)______/)_____\n|  |¯¯¯¯¯¯¯¯¯¯\)¯¯¯¯¯\)¯¯¯\n"

@app.route("/pruebasql")
def pruebasql():
	rows = junglebranchs.dbpg.selectTable("prueba","*","id = 1")
	return str(rows)
	
	
class prueba(Resource):
	def get(self):
		return "prueba"
api.add_resource(prueba, '/prueba')