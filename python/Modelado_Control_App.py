from bottle import *
import Modelado_Control as MC
import Modelado_Entidad as ME

initialized = False
modelParameters  = None
model = None

@route('/home')
def home():
    if modelParameters==None:
        return template('home')
    else:
        return template('home_initialized' )
@post('/home')
def createModel():
    modelParameters = ME.CollectionParameters()
    #modelParameters.setDocumentListPath("../matlab/matrix/DocumentsList.mat")
    #modelParameters.setDocumentListVariableName("LD")
    #modelParameters.setTextualFeaturesPath("../matlab/matrix/TF.mat")
    #modelParameters.setTextualFeaturesVariableName("TF")
    modelParameters.setTermDocumentMatrixPath(request.forms.TermDocumentMatrix.filename)
    modelParameters.setTermDocumentMatrixVariableName(request.forms.TermDocumentMatrixName)
    #modelParameters.setDocumentsPath("../data/images/")
    #modelParameters.setTextualFPath("../matlab/matrix/Ft.mat")
    #modelParameters.setTextualFVariableName("Ft")
    #modelParameters.setTextualHPath("../matlab/matrix/Ht.mat")
    #modelParameters.setTextualHVariableName("Ht")
    #modelParameters.setTextualVisualFPath("../matlab/matrix/FVt.mat")
    #modelParameters.setTextualVisualFVariableName("FVt")
    #modelParameters.setVisualFPath("../matlab/matrix/Fv.mat")
    #modelParameters.setVisualFVariableName("Fv")
    #modelParameters.setVisualHPath("../matlab/matrix/Hv.mat")
    #modelParameters.setVisualHVariableName("Hv")
    #modelParameters.setVisualTextualFPath("../matlab/matrix/FTv.mat")
    #modelParameters.setVisualTextualFVariableName("FTv")

    cC = MC.ControlCollection(modelParameters)

@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./')
run(host='localhost', port=9090, debug=True)

