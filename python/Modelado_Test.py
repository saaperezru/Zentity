
import Modelado_Control as MC
import Modelado_Entidad as ME

modelPa = ME.CollectionParameters()
modelPa.setDocumentListPath("../matlab/matrix/DocumentsList.mat")
modelPa.setDocumentListVariableName("LD")
modelPa.setTextualFeaturesPath("../matlab/matrix/TF.mat")
modelPa.setTextualFeaturesVariableName("TF")
modelPa.setTermDocumentMatrixPath("../matlab/matrix/TD.mat")
modelPa.setTermDocumentMatrixVariableName("TD")
modelPa.setDocumentsPath("../data/images/")
modelPa.setTextualFPath("../matlab/matrix/Ft.mat")
modelPa.setTextualFVariableName("Ft")
modelPa.setTextualHPath("../matlab/matrix/Ht.mat")
modelPa.setTextualHVariableName("Ht")
modelPa.setTextualVisualFPath("../matlab/matrix/FVt.mat")
modelPa.setTextualVisualFVariableName("FVt")
modelPa.setVisualFPath("../matlab/matrix/Fv.mat")
modelPa.setVisualFVariableName("Fv")
modelPa.setVisualHPath("../matlab/matrix/Hv.mat")
modelPa.setVisualHVariableName("Hv")
modelPa.setVisualTextualFPath("../matlab/matrix/FTv.mat")
modelPa.setVisualTextualFVariableName("FTv")

cC = MC.ControlCollection(modelPa)

tagsC = ME.TagsConfig(5,2,4)
ZPathsC = ME.ZentityPathsConfig("../data/code/","../data/zxml/","")
ControlZ = MC.ControlZentity("DMMTest1","RTTest1",cC,tagsC,ZPathsC) 
