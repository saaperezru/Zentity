from bottle import *
import Modelado_Control as MC
import Modelado_Entidad as ME

initialized = False
modelParameters  = None
model = None
cC = None
@route('/images')
def images():
    return template('images')
@route('/')
def home():
    if modelParameters==None:
        return template('home')
    else:
        return template('images' )
@post('/')
def createModel():
    modelParameters = ME.CollectionParameters()
    modelParameters.setDocumentListPath(request.forms.DocumentsList)
    modelParameters.setDocumentListVariableName(request.forms.DocumentsListName)
    modelParameters.setTextualFeaturesPath(request.forms.TextualFeaturesListName)
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

    cC = MC.ControlCollection(modelParameters)
    return template('images')


def showImages():
    info = cC.imageInfo()

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./')
run(host='localhost', port=9090, debug=True)

