from flask.views import MethodView 
from flask import Flask, jsonify

app=Flask(__name__)

class TestcaseApi(MethodView):
	def get(self):
		return jsonify({'Testcase0':'get'})

	def post(self):
		return jsonify({'Testcase1':'post'})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test/', methods=['POST','GET'])
def test():
    return 'Hello, World!'

app.add_url_rule('/Testcases/', view_func=TestcaseApi.as_view('Testcases'))

app.run(debug=True)