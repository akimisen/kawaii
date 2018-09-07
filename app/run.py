from flask.views import MethodView 
from flask import Flask, jsonify
from flask import request

app=Flask(__name__)

tasklist={
	'0':'task0',
	'1':'task1'
}

class TasklistApi(MethodView):
	def get(self):
		return jsonify(tasklist)

	def post(self):
		pass

class TaskApi(MethodView):
	def get(self,task_id):
		return jsonify({str(task_id):tasklist[str(task_id)]})

	def post(self):
		pass

@app.route('/api')
def api():
    return 'api'

def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
	shutdown_server()
	return 'Server shutting down...'

app.add_url_rule('/api/tasks', view_func=TasklistApi.as_view('tasklist'))
app.add_url_rule('/api/tasks/<int:task_id>', view_func=TaskApi.as_view('task'))

if __name__ == '__main__':
	app.run(debug=True)