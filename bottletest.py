from bottle import route, run

@route('/')
def hello():
    return "Hello World!"

run(host='0.0.0.0', port=9000, debug=True, reloader=True)
