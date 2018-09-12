from flask.views import MethodView 
from flask import Flask, jsonify, request, make_response
import logging
import json
import datetime

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

@app.route('/')
def index():
  return 'Hello,Wolld!'

@app.route('/api')
def api():
  return 'api'

@app.route('/test', methods=['GET','POST','OPTIONS'])
def test():
	params = request.json if request.method == "POST" else request.args
	try:
		response = make_response(jsonify(code=200, status=0, message='ok', data={}))
		response.headers['Access-Control-Allow-Origin'] = '*'
		response.headers['Access-Control-Allow-Methods'] = ['POST','OPTIONS']
		response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 
	except Exception as e:
		logging.exception(e)
	with open('tc {}.json'.format(datetime.datetime.now().strftime('%Y%m%d %H-%M-%S')),'w',encoding='gbk') as json_file:
		json.dump(params,json_file,ensure_ascii=False)
	return response

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