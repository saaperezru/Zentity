from bottle import *

initialized = False
modelParemeters = None


@route('/home')
def home():
    if modelParemeters==None:
        return template('home')
    else:
        return template('home_initialized' )
        
@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./')
run(host='localhost', port=9090, debug=True)

