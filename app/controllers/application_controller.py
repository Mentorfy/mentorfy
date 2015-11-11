from bottle import route, static_file 

def index():
    return static_file(filename='index.html', root='app/views', mimetype='text/html')

def images(filename):
    return static_file(filename, root='app/assets/images', mimetype='image/jpg')
