from bottle import *
from beaker.middleware import SessionMiddleware
import Modelado_Control as MC
import Modelado_Entidad as ME


session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './sessions',
    'session.auto': True
}

app = SessionMiddleware(app(), session_opts)

@route('/images')
def imagesDefault():
    return template('images')

@route('/images/<action>')
def images(action):
    s = request.environ.get('beaker.session')
    model = s.get('model',0)
    if action=="get":
        imgId = int(request.GET.get('id'))
        path,img = model.imagePath(imgId)
        #img = img + ".png"
	print "".join([path,img])
        return static_file(img, root=path)
    if action == "select":
        id = int(request.GET.get('id'))
        if request.GET.get('s')=="true":
            value = True
        else:
            value = False
        if id<0: 
            abort(400,"Bad GET parameters")
        docsList = model.getDocumentsList()
        img = docsList[min(id,len(docsList))]
        img.setSelected(value)
	return
    if action == "list":
        images = []
        #setting json as MIME type
        response.set_header('Content-Type','application/json')
        docsList = model.getDocumentsList()
        for i in range(len(docsList)):
            images.append({"imgId": i,"selected":docsList[i].getSelected()})
        return {"images" : images}
    abort(400,"Bad GET parameters")

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/')
@route('/')
def home():
    s = request.environ.get('beaker.session')
    model = s.get('model',0)
    print "[DEBUG]",model
    if not model:
        return template('home')
    else:
        redirect('/images')
@post('/')
def createModel():
    modelParameters = ME.CollectionParameters()
    modelParameters.setDocumentListPath(request.forms.DocumentsList)
    modelParameters.setDocumentListVariableName(request.forms.DocumentsListName)
    modelParameters.setTextualFeaturesPath(request.forms.TextualFeaturesList)
    modelParameters.setTextualFeaturesVariableName(request.forms.TextualFeaturesListName)
    modelParameters.setTermDocumentMatrixPath(request.forms.TermDocumentMatrix)
    modelParameters.setTermDocumentMatrixVariableName(request.forms.TermDocumentMatrixName)
    modelParameters.setDocumentsPath(request.forms.DocumentsPath)
    modelParameters.setTextualFPath(request.forms.TextualF)
    modelParameters.setTextualFVariableName(request.forms.TextualFName)
    modelParameters.setTextualHPath(request.forms.TextualH)
    modelParameters.setTextualHVariableName(request.forms.TextualHName)
    modelParameters.setTextualVisualFPath(request.forms.TextualVisualF)
    modelParameters.setTextualVisualFVariableName(request.forms.TextualVisualFName)
    modelParameters.setVisualFPath(request.forms.VisualF)
    modelParameters.setVisualFVariableName(request.forms.VisualFName)
    modelParameters.setVisualHPath(request.forms.VisualH)
    modelParameters.setVisualHVariableName(request.forms.VisualHName)
    modelParameters.setVisualTextualFPath(request.forms.VisualTextualF)
    modelParameters.setVisualTextualFVariableName(request.forms.VisualTextualFName)
    try:
        s = request.environ.get('beaker.session')
        s['model'] = MC.ControlCollection(modelParameters)
        s.save()
    except:
        abort(400,"ERROR!!!!")
    redirect('/images')

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./static')
run(host='localhost', port=9090, debug=True, app=app)
