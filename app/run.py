from flask.views import MethodView
from flask import Flask, jsonify, request, make_response
import logging
import json
import datetime
from pymongo import MongoClient

app=Flask(__name__)

tasklist=[
	{'jira1':'secxxxx','jira2':'stestxxx','pkg':'专题包xx','module':'管理','version':'1.9.1.0','status':False}
	]
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class TasklistApi(MethodView):
	def get(self):
		response = make_response(jsonify(tasklist))
		response.headers['Access-Control-Allow-Origin'] = '*'
		response.headers['Access-Control-Allow-Methods'] = ['GET','POST']
		response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
		return response

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

@app.route('/api', methods=['GET','POST'])
def api():
	if request.method:
		params = request.get_json(force=True)
		api = params['api']
		try:
			response = make_response(jsonify(code=200, status=0, message='ok', data={'api':api}))
			response.headers['Access-Control-Allow-Origin'] = '*'
			response.headers['Access-Control-Allow-Methods'] = ['GET','POST']
			response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
		except Exception as e:
			logging.exception(e)

		try:
			conn = MongoClient(host='localhost', port=27017)
			col = conn.kawaii[api]
			insert_data=params
			insert_data['datetime']=datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
			col.insert_one(insert_data)
		except Exception as e:
			logging.exception(e)
		finally:
			conn.close()
		# # with open('tc {}.json'.),'w',encoding='gbk') as json_file:
		# # 	json.dump(params,json_file,ensure_ascii=False)
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

