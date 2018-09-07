from flask.views import MethodView 
from flask import Flask, jsonify

app=Flask(__name__)

class TaskApi(MethodView):
	def get(self):
		return jsonify({'task0':'get'})

	def post(self):
		return jsonify({'task1':'post'})

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.add_url_rule('/tasks/', view_func=TaskApi.as_view('tasks'))

app.run(debug=True)