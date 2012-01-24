#T (20x20) = (20x10)(10x20)
#V(20x20) = (20x9(9x20)

import Modelado_Control as MC
import Modelado_Entidad as ME

modelPa = ME.CollectionParameters()
modelPa.setDocumentListPath("../matlab/matrix/DL.mat")
modelPa.setDocumentListVariableName("DL")
modelPa.setTextualFeaturesPath("../matlab/matrix/TF.mat")
modelPa.setTextualFeaturesVariableName("TF")
modelPa.setTermDocumentMatrixPath("../matlab/matrix/TD.mat")
modelPa.setTermDocumentMatrixVariableName("TD")
modelPa.setDocumentsPath("./documentsFolder/")
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

cC = MC.ControlCollection()
cC.beginCollection(modelPa)
