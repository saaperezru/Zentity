from bottle import *
import Modelado_Control as MC
import Modelado_Entidad as ME

initialized = False
modelParameters  = None
model = None
cC = None

@route('/home')
def home():
    if modelParameters==None:
        return template('home')
    else:
        return template('images' )
@post('/home')
def createModel():
    modelParameters = ME.CollectionParameters()
    modelParameters.setDocumentListPath(request.files.DocumentsList.filename)
    modelParameters.setDocumentListVariableName(request.forms.DocumentsListName)
    modelParameters.setTextualFeaturesPath(request.files.TextualFeaturesListName.filename)
    modelParameters.setTextualFeaturesVariableName(request.forms.TextualFeaturesListName)
    modelParameters.setTermDocumentMatrixPath(request.files.TermDocumentMatrix.filename)
    modelParameters.setTermDocumentMatrixVariableName(request.forms.TermDocumentMatrixName)
    modelParameters.setDocumentsPath(request.forms.DocumentsPath)
    modelParameters.setTextualFPath(request.files.TextualF.filename)
    modelParameters.setTextualFVariableName(request.forms.TextualFName)
    modelParameters.setTextualHPath(request.files.TextualH.filename)
    modelParameters.setTextualHVariableName(request.forms.TextualHName)
    modelParameters.setTextualVisualFPath(request.files.TextualVisualF.filename)
    modelParameters.setTextualVisualFVariableName(request.forms.TextualVisualFName)
    modelParameters.setVisualFPath(request.files.VisualF.filename)
    modelParameters.setVisualFVariableName(request.forms.VisualFName)
    modelParameters.setVisualHPath(request.files.VisualH.filename)
    modelParameters.setVisualHVariableName(request.files.VisualHName)
    modelParameters.setVisualTextualFPath(request.files.VisualTextualF.filename)
    modelParameters.setVisualTextualFVariableName(request.forms.VisualTextualFName)

    cC = MC.ControlCollection(modelParameters)
    return template('images')


def showImages():
    info = cC.imageInfo()

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./')
run(host='localhost', port=9090, debug=True)

