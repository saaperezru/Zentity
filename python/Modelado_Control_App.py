from bottle import *
from beaker.middleware import SessionMiddleware
import Modelado_Control as MC
import Modelado_Entidad as ME


session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 999,
    'session.data_dir': './sessions',
    'session.auto': True
}

app = SessionMiddleware(app(), session_opts)

@route('/images')
def imagesDefault():
    return template('images')
@route('/latentTopics')
def latentTopDefault():
    return template('latentTopics')
@route('/codeGenerator')
def codeGeneratorDefault():
    return template('codeGenerator')
@route('/latentTopics/<action>')
def latentTopics(action):
    s = request.environ.get('beaker.session')
    model = s.get('model',0)
    if action == "select":
        id = int(request.GET.get('id'))
        type = request.GET.get('type')
        if request.GET.get('s')=="true":
            value = True
        else:
            value = False
        if id<0:
            abort(400,"Bad GET parameters")
        if type=="textual":
            LTSStatus = model.getCollection().getSelectedTextualLatentTopics()
        else:
            LTSStatus = model.getCollection().getSelectedVisualLatentTopics()
        LTSStatus[id]=value
        return
    if action == "list":
        numberOfImages = 5
        numberOfWordsInLTName = 7
        LTS = []
        #setting json as MIME type
        response.set_header('Content-Type','application/json')
        #Construction of Textual LTS information array
        LTSList = model.getControlNMFTextual().getControlArrayLatentTopics()
        LTSStatus = model.getCollection().getSelectedTextualLatentTopics()
        controlLT = model.getControlNMFTextual()
        for i in range(len(LTSList)):
            LTS.append({"lid":i,"name": controlLT.names(LTSList[i],numberOfWordsInLTName,True),"type":"textual","selected":LTSStatus[i],"docs":controlLT.images(LTSList[i],numberOfImages)})
        #Construction of Visual LTS information array
        LTSList = model.getControlNMFVisual().getControlArrayLatentTopics()
        LTSStatus = model.getCollection().getSelectedVisualLatentTopics()
        controlLT = model.getControlNMFVisual()
        for i in range(len(LTSList)):
            LTS.append({"lid":i,"name": controlLT.names(LTSList[i],numberOfWordsInLTName,False),"type":"visual","selected":LTSStatus[i],"docs":controlLT.images(LTSList[i],numberOfImages)})
        return {"LTS" : LTS}
    abort(400,"Bad GET parameters")

@route('/images/<action>')
def images(action):
    s = request.environ.get('beaker.session')
    model = s.get('model',0)
    if action=="get":
        imgId = int(request.GET.get('id'))
        path,img = model.imagePath(imgId)
        if img[-3:].lower() != "jpg" and img[-3:].lower() != "png":
            img = img + ".jpeg"
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
@get('/')
def home():
    s = request.environ.get('beaker.session')
    model = s.get('model',0)
    print "[DEBUG]",model
    if request.GET.get('action')=="reset":
        s['model'] = 0
        s.save()
        redirect('/')
    if not model:
        return template('home')
    else:
        return template('home_initialized')
@post('/')
def createModel():
    s = request.environ.get('beaker.session')
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
        s['model'] = MC.ControlCollection(modelParameters)
        s.persist()
        s.save()
    except:
        raise
        abort(400,"ERROR!!!!")
    redirect('/images')

@post('/codeGenerator/<action>')
def createZentityModel(action):
    s = request.environ.get('beaker.session')
    if action == "generate":
        model = s.get('model',0)
        tagsC = ME.TagsConfig(int(request.forms.topWords), int(request.forms.LTNamesTop), int(request.forms.LTNamesSize))
        ZPathsC = ME.ZentityPathsConfig(request.forms.codeStoragePath, request.forms.zxmlFilesPath, request.forms.xmlInfoPath)
        ControlZ = MC.ControlZentity(request.forms.dataModelName, request.forms.resourceTypeName,model,tagsC,ZPathsC)
        try:
            ControlZ.generateCode()
            ControlZ.generateUploadingCode()
            ControlZ.generateZXMLFiles()
            del ControlZ
            return template("codeGenerator_sucess")
        except:
            raise
            abort(400,"ERROR!!!!")


@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./static')
run(host='localhost', port=9090, debug=True, app=app)
