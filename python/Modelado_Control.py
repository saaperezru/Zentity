#import Modelado_Entidad_ExtractorsRenata as Extractors
import numpy as np
import scipy.io as sio
import InterfazNMF_Control as INMFC
import InterfazZ_Entidad as ZEntidad
import InterfazZ_Control as ZControl
import Modelado_Entidad as Entidad


class ControlMatrix:

    @staticmethod
    def InstanceMatrix(path,name):
        return np.array(sio.loadmat(path)[name])
        
class ControlCollection:
    
    def __init__(self):
        self.__controlZentity = None
        self.__controlNMFTextual = None
        self.__controlNMFVisual = None
        self.__collection = None
    
    def __init__(self,colectionParameters):
        try:
            self.__controlZentity = None
        
            #Latent Topics creation
            documentList = ControlMatrix.InstanceMatrix(colectionParameters.getDocumentListPath(), colectionParameters.getDocumentListVariableName())
            textualF = ControlMatrix.InstanceMatrix(colectionParameters.getTextualFPath(), colectionParameters.getTextualFVariableName()) 
            textualH = ControlMatrix.InstanceMatrix(colectionParameters.getTextualHPath(), colectionParameters.getTextualHVariableName())
            textualVisualF = ControlMatrix.InstanceMatrix(colectionParameters.getTextualVisualFPath(), colectionParameters.getTextualVisualFVariableName())
            self.__controlNMFTextual = ControlNMF(self,textualF,textualH, textualVisualF, documentList, 1, "Textual", "Tex")

	    visualF = ControlMatrix.InstanceMatrix(colectionParameters.getVisualFPath(), colectionParameters.getVisualFVariableName())
            visualH = ControlMatrix.InstanceMatrix(colectionParameters.getVisualHPath(), colectionParameters.getVisualHVariableName())
            visualTextualF = ControlMatrix.InstanceMatrix(colectionParameters.getVisualTextualFPath(), colectionParameters.getVisualTextualFVariableName())
            self.__controlNMFVisual = ControlNMF(self, visualF, visualH, visualTextualF, documentList, 2, "Visual", "Vis")

            #Collection creation
            textualFeatures = ControlMatrix.InstanceMatrix(colectionParameters.getTextualFeaturesPath(), colectionParameters.getTextualFeaturesVariableName())
            tF=[]
            for i in  textualFeatures.tolist():
	        tF.append(i[0][0])
            termDocumentMatrix = ControlMatrix.InstanceMatrix(colectionParameters.getTermDocumentMatrixPath(), colectionParameters.getTermDocumentMatrixVariableName())
            documents = []
            k = 0
            if documentList.shape[0] == 1:
                documentList = np.transpose(documentList)
            for i in documentList.tolist():
                tags = []
                for j in xrange(0, textualFeatures.shape[0]):
                    if(termDocumentMatrix[j,k]==1):
                        tags.add(tf[j])
                documents.append(Entidad.Document(i[0][0],tags,True))
                k = k + 1
            self.__collection = Entidad.Collection(documents, range(0,textualF.shape[1]), range(0,visualF.shape[1]), tF, termDocumentMatrix, None, colectionParameters.getDocumentsPath())
        except:
            print "Error-creation"
        
    def imageInfo(self):
        if(self.__collection == None):
            return None
        else:
            return (self.__collection.getDocuments(),self.__collection.getDocumentsPath())
    def latentTopicsInfo(self):
        if(self.__collection == None or self.__controlNMFTextual == None):
            return None
        else:
            #FALTA
            return (self.__collection.getTextualFeatures(),self.__collection.getDocuments(),self.__collection.getDocumentsPath())
            
class ControlNMF:

    def __init__(self, controlCollection, f, h, mf, documents, id, name, abreviature):
        self.__controlCollection = controlCollection
        self.__controlLatentTopics = INMFC.ControlTypeLatentTopic(id, name, abreviature, documents, h, f, None, mf,None)
        if (self.__controlLatentTopics == None):
            raise Exception()
        
    def images(self):
        pass
    
    def names(self):
        pass
        
class ControlZentity:
    
    def __init__(self,DMMName,RTName,Control,topWords,LTNameTop,codeStoragePath,zxmlFilesPath,xmlInfoPath):
        """Builds an interface to communicate with InterfazZ to create a model with the detected LatentTopics
        
        Attributes:
        
            - DMMName -- Name for the Data Model Module, it must be unique among the names of DMMs present in the Zentity instance
            - RTName -- Name for the Resource Type that will shelter all the images in the collection. NOTE: It must be unque among all the Resource TYpes in all the Data Model Modules in the Zentity instance that will be used
            - Conrtol -- An instance of the ControlCollection that creates this ControlZentity
            - xmlInfoPath
        """
        self.codeStoragePath = codeStoragePath
        self.zxmlDirectory = zxmlFilesPath
        #Lets create the DMM
        self.DMM = ZEntidad.DataModelModule(DMMName)
        #And the only RT we will need
        RT1 = ZEntidad.ResourceType(RTName)
        #We must define an XMLStructure for the ZXML files
        RT1.setXMLStructure(ZEntidad.XMLStructure("ParentImages","Image","Images"))
        #As well as a VisualizationType
        RT1.setVisualizationType(Entidad.VisualizationType(Entidad.VisualizationType.IMAGE,Control.collection.getImagesPath()))
        #And all documents as instances of this DMM
        for doc in Control.collection.getDocuments():
            RT1.addInstance(doc.id)
        #Finally we add this Resource Type to the DMM Model
        DMM.addResourceType(RT1)
        #Now add al  the Scalar Properties to this RT1
        #Some basic SPs
        titleExtractor = Extractors.TitleExtractor(xmlInfoPath)
        RT1.addProperty(ZEntidad.ScalarProperty("Title",ZEntidad.DataTYpes.STRING,titleExtractor,False,True))
        descriptionExtractor = Extractors.DescriptionExtractor()
        RT1.addProperty(ZEntidad.ScalarProperty("Description",ZEntidad.DataTYpes.STRING,descriptionExtractor,False,True))
        mainCategoryExtractor = Extractors.MainCategoryExtractor() 
        RT1.addProperty(ZEntidad.ScalarProperty("Main_Category",ZEntidad.DataTYpes.STRING,mainCategoryExtractor))
        #There is one SP for each Textual LatentTopic 
        for LT in Control.
        #There is one SP for each Visual LatentTopic 
        
        #There is one SP for each ImportantTag
        for tag in self.detectMostImportantTextualWords(topWords,LTNameTop):
            tagExtractor = Entidad.TagExtractor(tag,)
            RT1.addProperty(ZEntidad.ScalarProperty("Tag_"+tag,ZEntidad.DataTYpes.STRING,tagExtractor,False,True))
        #Finally lets generate the Code Generator
        self.Gen = Control.CodeGenerator(DMM,self.codeStoragePath)
        

    
    def generateCode():
        self.Gen.saveGenerationCode()
        
    def generateUploadingCode():
        self.Gen.saveInsertionCode(self.zxmlDirectory)
        
    def generateZXMLFiles():
        ZXML = Control.ZXMLGenerator(self.DMM,self.zxmlDirectory)
        ZXML.save()
        
        
    def detectMostImportantTextualWords(top,LTNamesTop):
        """Detects the most important textual words according to this criterion:
            * The <top> most used words are considered important
            * The first <LTNamesTop> in the name of all the Latent Topics are important
            
            Attributes:
                - top -- The number of words that will be considered important in a list of descendent images by 
                - LTNamesTop -- The number of words that will be taken from the Latent TOpic names
            Return:
                A list of strings
        """
    
        pass
