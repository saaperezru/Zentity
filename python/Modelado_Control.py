#import Modelado_Entidad_ExtractorsRenata as Extractors
import Modelado_Entidad_DummyExtractors as Extractors
import numpy as np
import scipy.io as sio
import InterfazNMF_Control as INMFC
import InterfazZ_Entidad as ZEntidad
import InterfazZ_Control as ZControl
import Modelado_Entidad as Entidad

class ControlMatrix:

    @staticmethod
    def InstanceMatrix(path, name):
        """Import a Matlab matrix.
           Parameters:
               - path -- Path and file where is saved the matrix 
               - name -- Name of the Matlab matrix.
           Return:
               A numpy array with all elements of the Matlab matrix.
        """
        return np.array(sio.loadmat(path)[name])
        
class ControlCollection:
    
    def __init__(self, colectionParameters):
        """Is the control class of Modelado. It is responsible for building and modifying the data model.
           Parameters
               - colectionParameters -- Especial data object with all parameters needed for construct the model.
           Attributes
              - controlNMFTextual -- Interfaz NMF object with all information about textual latent topics.
              - controlNMFVisual -- Interfaz NMF object with all information about visual latent topics.
              - collection -- Model object the save the information of the documents, tags, selected latent topics, etc. 
        """
        try:
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
            #Creating tag array
            textualFeatures = ControlMatrix.InstanceMatrix(colectionParameters.getTextualFeaturesPath(), colectionParameters.getTextualFeaturesVariableName())
            if(textualFeatures.shape[0] < textualFeatures.shape[1]):
                textualFeatures = np.transpose(textualFeatures)
            if(textualFeatures.shape[1] != 1):
                #FALTA CREAR LA EXEPCION
                raise
            tF=[]
            for i in  textualFeatures.tolist():
	        tF.append(i[0][0])
            termDocumentMatrix = ControlMatrix.InstanceMatrix(colectionParameters.getTermDocumentMatrixPath(), colectionParameters.getTermDocumentMatrixVariableName())
            
            #Lets create the ordered tags list
            tagsOcurrence = np.dot(termDocumentMatrix,np.ones((termDocumentMatrix.shape[1],1)))
            orderedTags = np.argsort(tagsOcurrence)
            
            #Documents creation
            documents = []
            k = 0
            if documentList.shape[0] == 1:
                documentList = np.transpose(documentList)
            for i in documentList.tolist():
                tags = []
                for j in xrange(0, textualFeatures.shape[0]):
                    if(termDocumentMatrix[j,k]>0):
                        tags.append(tF[j])
                documents.append(Entidad.Document(i[0][0],tags,True))
                k = k + 1
            self.__collection = Entidad.Collection(documents, range(0,textualF.shape[1]), range(0,visualF.shape[1]), tF, orderedTags, termDocumentMatrix, colectionParameters.getDocumentsPath())
        except:
            print "Error-creation"
            #FALTA CREAR LA EXEPCION
            raise
        
    def imageInfo(self):
        """Returns information about all documents in the model."""
        if(self.__collection == None):
            return None
        else:
            return self.__collection.getDocuments(),self.__collection.getDocumentsPath()
    
    def latentTopicsInfo(self):
        pass
    
    def getDocument(self, idm):
        """Returns the document instance."""
        if(self.__collection == None):
            return None
        else:
            # We use the built-in method from ControlNMF for getting the position of a document, given only the id, in the matrix
            return self.__collection.getDocuments()[self.__controlNMFTextual.getDocumentPosition(idm)]
    
    def getOrderedTags(self, amount):
        """Given an amount of tags, return the most important used in the documents.
           Parameters:
               - amount --  the number of tags that it would be returned.
           Return:
               A list of tags(strings).  
        """
        ret = []
        for i in range(amount):
           ret.append(self.__collection.getTextualFeatures()[self.__collection.getOrderedTags()[i]])
        return ret
    
    def getCollection(self):
        """Returns the collection instance."""
        return self.__collection
    
    def getControlNMFTextual(self):
        """Returns the controlNMFTextual instance."""
        return self.__controlNMFTextual 
    
    def getControlNMFVisual(self):
        """Returns the controlNMFVisual instance."""
        return self.__controlNMFVisual
            
class ControlNMF:

    def __init__(self, controlCollection, f, h, mf, documents, id, name, abreviature):
        self.__controlCollection = controlCollection
        self.__controlLatentTopics = INMFC.ControlTypeLatentTopic(id, name, abreviature, documents, h, f, None, mf,None)
        if (self.__controlLatentTopics == None):
            raise Exception()
        
    def mostImportantLatentTopic(self,id):
        return self.__controlLatentTopics.getLatentTopicsForImg(id)[0]
    
    def images(self,controlLatentTopic,tam):
        """Return top <tam> most important string array for the given laten topic."""
        importatNames = controlLatentTopic.getDocumentResume()
        images = []
        for i in xrange(0,tam):
            images.append(self.__controlCollection.getCollection.getDocuments()[importatNames[i]])
        return images   
    
    def names(self,controlLatentTopic,tam):
        """Retorn top <tam> most important string array for the given laten topic.
        """
        importatNames = controlLatentTopic.getModalResume()
        name = []
        for i in xrange(0,tam):
            name.append(self.__controlCollection.getCollection().getTextualFeatures()[importatNames[i]])
        return name
    def getControlArrayLatentTopics(self):
        return self.__controlLatentTopics.getControlArrayLatentTopics()
    def getDocumentPosition(self,idm):
        return self.__controlLatentTopics.getDictionary(idm)

class ControlZentity:
    
    def __init__(self,DMMName,RTName,collectionControl,tagsConfig,zentityPaths):
        """Builds an interface to communicate with InterfazZ to create a model with the detected LatentTopics
        
        Attributes:
        
            - DMMName -- Name for the Data Model Module, it must be unique among the names of DMMs present in the Zentity instance
            - RTName -- Name for the Resource Type that will shelter all the images in the collection. NOTE: It must be unque among all the Resource TYpes in all the Data Model Modules in the Zentity instance that will be used
            - Conrtol -- An instance of the ControlCollection that creates this ControlZentity
            - xmlInfoPath
        """
        topWords = tagsConfig.topWords
        LTNameTop = tagsConfig.LTNamesTop
        LatentTopicsNameSize = tagsConfig.LTNamesSize
        codeStoragePath = zentityPaths.codePath
        zxmlFilesPath = zentityPaths.zxmlPath
        xmlInfoPath = zentityPaths.xmlPath
        self.controlCollection = collectionControl
        self.codeStoragePath = codeStoragePath
        self.zxmlDirectory = zxmlFilesPath
        self.importantTags = set()
        #Lets create the DMM
        self.DMM = ZEntidad.DataModelModule(DMMName)
        #And the only RT we will need
        RT1 = ZEntidad.ResourceType(RTName)
        #We must define an XMLStructure for the ZXML files
        RT1.setXMLStructure(ZEntidad.XMLStructure("ParentImages","Image","Images"))
        #As well as a VisualizationType
        RT1.setVisualizationType(ZEntidad.VisualizationType(ZEntidad.VisualizationType.IMAGE,self.controlCollection.getCollection().getDocumentsPath()))
        #And all documents as instances of this DMM
        for doc in self.controlCollection.getCollection().getDocuments():
            if doc.getSelected():
                RT1.addInstance(doc.getId())
        #Finally we add this Resource Type to the DMM Model
        self.DMM.addResourceType(RT1)
        #Now add al  the Scalar Properties to this RT1
        #Some basic SPs
        titleExtractor = Extractors.TitleExtractor(xmlInfoPath)
        RT1.addProperty(ZEntidad.ScalarProperty("Title",ZEntidad.DataTypes.STRING,titleExtractor,False,True))
        descriptionExtractor = Extractors.DescriptionExtractor(xmlInfoPath)
        RT1.addProperty(ZEntidad.ScalarProperty("Description",ZEntidad.DataTypes.STRING,descriptionExtractor,False,True))
        #A main textual category extractor
        mainTextualCategoryExtractor = Extractors.MainCategoryExtractor(self.controlCollection.getControlNMFTextual(),LatentTopicsNameSize ) 
        RT1.addProperty(ZEntidad.ScalarProperty("Main_Textual_Category",ZEntidad.DataTypes.STRING,mainTextualCategoryExtractor))
        #A main visual category extractor
        mainVisualCategoryExtractor = Extractors.MainCategoryExtractor(self.controlCollection.getControlNMFVisual(),LatentTopicsNameSize ) 
        RT1.addProperty(ZEntidad.ScalarProperty("Main_Visual_Category",ZEntidad.DataTypes.STRING,mainVisualCategoryExtractor))
        #There must be one identifier property
        imageIdExtractor = Extractors.ImageIdExtractor()
        RT1.addProperty(ZEntidad.ScalarProperty("ImageID",ZEntidad.DataTypes.STRING,imageIdExtractor,True,False))
        #There is one SP for each Visual LatentTopic 
        for LT in self.controlCollection.getControlNMFVisual().getControlArrayLatentTopics():
            LTExtractor = Extractors.LatentTopicExtractor(LT)
            LTName = self.controlCollection.getControlNMFVisual().names(LT,LatentTopicsNameSize)
            for i in range(min(LTNameTop,len(LTName))):
                self.importantTags.add(LTName[i])
            LTName.insert(0,"LTT")
            RT1.addProperty(ZEntidad.ScalarProperty("_".join(LTName),ZEntidad.DataTypes.STRING,LTExtractor))
        #There is one SP for each Textual LatentTopic 

        for LT in self.controlCollection.getControlNMFTextual().getControlArrayLatentTopics():
            LTExtractor = Extractors.LatentTopicExtractor(LT)
            LTName = self.controlCollection.getControlNMFTextual().names(LT,LatentTopicsNameSize)
            for i in range(min(LTNameTop,len(LTName))):
                self.importantTags.add(LTName[i])
            LTName.insert(0,"LTV")
            RT1.addProperty(ZEntidad.ScalarProperty("_".join(LTName),ZEntidad.DataTypes.STRING,LTExtractor))
        
        #There is one SP for each ImportantTag
        for tag in self.detectMostImportantTextualWords(topWords):
            tagExtractor = Extractors.TagExtractor(tag,self.controlCollection)
            RT1.addProperty(ZEntidad.ScalarProperty("Tag_"+tag,ZEntidad.DataTypes.STRING,tagExtractor))
        #Finally lets generate the Code Generator
        self.Gen = ZControl.CodeGenerator(self.DMM,self.codeStoragePath)
        

    
    def generateCode(self):
        self.Gen.saveGenerationCode()
        
    def generateUploadingCode(self):
        self.Gen.saveInsertionCode(self.zxmlDirectory)
        
    def generateZXMLFiles(self):
        ZXML = ZControl.ZXMLGenerator(self.DMM,self.zxmlDirectory)
        ZXML.save()
        
        
    def detectMostImportantTextualWords(self,top):
        """Detects the most important textual words according to this criterion:
            * The <top> most used words are considered important
            * The first <LTNamesTop> in the name of all the Latent Topics are important
            
            Attributes:
                - top -- The number of words that will be considered important in a list of descendent images by 
                - LTNamesTop -- The number of words that will be taken from the Latent TOpic names
            Return:
                A list of strings
        """
        for t in self.controlCollection.getOrderedTags(top):
            self.importantTags.add(t)
        return list(self.importantTags)
