from numpy import *

class Document:
     
    def __init__(self, id, tags, selected):
        """Is a model class, it save all information of a document.
           Attributes
              - id -- Interfaz NMF object with all information about textual latent topics.
              - tags -- Interfaz NMF object with all information about visual latent topics.
              - selected -- Boolean attribute, it is true if the document is selected for the Zentity collection, false otherwise. 
        """
        self.__id = id
        self.__tags = tags
        self.__selected = selected   
    
    #Getters for each attributes
    def getId(self):
        """ Returns the LatentTopic Id.
        """
        return self.__id
    def getTags(self):
        """ Returns the Tags of the document.
        """
        return self.__tags
    def getSelected(self):
        """ Returns True if the document is selected, False otherwise.
        """
        return self.__selected
    
   
    #set method for the only attribute that can change.
    def setSelected(self, selected):
        """ Save selected variable.
        """
        self.__selected = selected
   


class Collection:
     
    def __init__(self, documents, selectedTextualLatentTopics, selectedVisualLatentTopics, textualFeatures, orderedTags, termDocumentMatrix, documentsPath):
        """Is a model class, it save all collection information as document list, selected latent topics, textual features and others.
           Attributes
              - documents -- List of all documents.
              - selectedTextualLatentTopics -- Index list of selected textual latent topics.
              - selectedVisualLatentTopics -- Index list of selected visual latent topics.
              - textualFeatures -- String list of textual words or tags.
              - orderedTags -- Order index list of the most important tags.
              - termDocumentMatrix -- Term vs Document matrix used in the NMF factorization.
              - documentsPath -- Folder path of all images.
        """
        self.__documents = documents
        self.__selectedTextualLatentTopics = selectedTextualLatentTopics
        self.__selectedVisualLatentTopics = selectedVisualLatentTopics
        self.__textualFeatures = textualFeatures
        self.__orderedTags = orderedTags
        self.__termDocumentMatrix = termDocumentMatrix 
        self.__documentsPath = documentsPath   
    
    #Getters for each attributes
    def getDocuments(self):
        """ Returns the complete array of documents.
        """
        return self.__documents
    def getSelectedTextualLatentTopics(self):
        """ Returns the selected latent topics.
        """
        return self.__selectedTextualLatentTopics
    def getSelectedVisualLatentTopics(self):
        """ Returns the selected latent topics.
        """
        return self.__selectedVisualLatentTopics
    def getTextualFeatures(self):
        """ Returns the textual words used.
        """
        return self.__textualFeatures
    def getOrderedTags(self):
        """ Returns the textual words used.
        """
        return self.__orderedTags
    def getTermDocumentMatrix(self):
        """ Returns the term vs  Document matrix.
        """
        return self.__termDocumentMatrix
    def getDocumentsPath(self):
        """ Returns the images path in string format.
        """
        return self.__documentsPath
    
   
    #set method for the only attribute that can change.
    def setSelectedTextualLatentTopics(self, selectedTextualLatentTopics):
        """ Save selectedTextualLatentTopics variable.
        """
        self.__selectedTextualLatentTopics = selectedTextualLatentTopics
    def setSelectedVisualLatentTopics(self, selectedVisualLatentTopics):
        """ Save selectedVisualLatentTopics variable.
        """
        self.__selectedVisualLatentTopics = selectedVisualLatentTopics

class CollectionParameters:
     
    def __init__(self):
        "Especial data object. It save the initial information given for the user, and it is used to construct the ControlCollection object."
        self.__documentListPath = None
        self.__documentListVariableName = None
        self.__textualFeaturesPath = None
        self.__textualFeaturesVariableName = None
        self.__termDocumentMatrixPath = None
        self.__termDocumentMatrixVariableName = None
        self.__documentsPath = None
        self.__textualFPath = None
        self.__textualFVariableName = None
        self.__textualHPath = None
        self.__textualHVariableName = None
        self.__textualVisualFPath = None
        self.__textualVisualFVariableName = None
        self.__visualFPath = None
        self.__visualFVariableName = None
        self.__visualHPath = None
        self.__visualHVariableName = None
        self.__visualTextualFPath = None
        self.__visualTextualFVariableName = None
        
        
    #Getters for each attributes
    def getDocumentListPath(self):
        """ Returns the path of the document list.
        """
        return self.__documentListPath
    def getDocumentListVariableName(self):
        """ Returns the name of the document list variable.
        """
        return self.__documentListVariableName
    def getTextualFeaturesPath(self):
        """ Returns the path of the textual words.
        """
        return self.__textualFeaturesPath
    def getTextualFeaturesVariableName(self):
        """ Returns the variable name of the textualFeatures matrix.
        """
        return self.__textualFeaturesVariableName
    def getTermDocumentMatrixPath(self):
        """ Returns the path of the term vs Document Matrix.
        """
        return self.__termDocumentMatrixPath
    def getTermDocumentMatrixVariableName(self):
        """ Returns the variable name of the term vs Document matrix.
        """
        return self.__termDocumentMatrixVariableName
    def getDocumentsPath(self):
        """ Returns the path of the documents folder.
        """
        return self.__documentsPath
    def getTextualFPath(self):
        """ Returns the path of the textual F matrix.
        """
        return self.__textualFPath
    def getTextualFVariableName(self):
        """ Returns the variable name of the textual F matrix.
        """
        return self.__textualFVariableName
    def getTextualHPath(self):
        """ Returns the path of the textual H matrix.
        """
        return self.__textualHPath
    def getTextualHVariableName(self):
        """ Returns the variable name of the textual H matrix.
        """
        return self.__textualHVariableName
    def getTextualVisualFPath(self):
        """ Returns the path of the visual matrix F in the asymmetric NMF.
        """
        return self.__textualVisualFPath
    def getTextualVisualFVariableName(self):
        """ Returns the variable name of the visual matrix F in the asymmetric NMF.
        """
        return self.__textualVisualFVariableName
    def getVisualFPath(self):
        """ Returns the path of the visual F matrix.
        """
        return self.__visualFPath
    def getVisualFVariableName(self):
        """ Returns the variable name of the visual F matrix.
        """
        return self.__visualFVariableName
    def getVisualHPath(self):
        """ Returns the path of the visual H matrix.
        """
        return self.__visualHPath
    def getVisualHVariableName(self):
        """ Returns the variable name of the visual H matrix.
        """
        return self.__visualHVariableName
    def getVisualTextualFPath(self):
        """ Returns the path of the textual matrix F in the asymmetric NMF.
        """
        return self.__visualTextualFPath
    def getVisualTextualFVariableName(self):
        """ Returns the variable name of the textual matrix F in the asymmetric NMF.
        """
        return self.__visualTextualFVariableName
    
   
    #set method for the only attribute that can change.
    def setDocumentListPath(self, documentListPath):
        """ Save documentListPath variable.
        """
        self.__documentListPath = documentListPath
    def setDocumentListVariableName(self, documentListVariableName):
        """ Save documentListVariableName variable.
        """
        self.__documentListVariableName = documentListVariableName
    def setTextualFeaturesPath(self, textualFeaturesPath):
        """ Save textualFeaturesPath variable.
        """
        self.__textualFeaturesPath = textualFeaturesPath
    def setTextualFeaturesVariableName(self, textualFeaturesVariableName):
        """ Save textualFeaturesVariableName variable.
        """
        self.__textualFeaturesVariableName = textualFeaturesVariableName
    def setTermDocumentMatrixPath(self, termDocumentMatrixPath):
        """ Save termDocumentMatrixPath variable.
        """
        self.__termDocumentMatrixPath = termDocumentMatrixPath
    def setTermDocumentMatrixVariableName(self, termDocumentMatrixVariableName):
        """ Save termDocumentMatrixVariableName variable.
        """
        self.__termDocumentMatrixVariableName = termDocumentMatrixVariableName
    def setDocumentsPath(self, documentsPath):
        """ Save termDocumentMatrixPath variable.
        """
        self.__documentsPath = documentsPath
    def setTextualFPath(self, textualFPath):
        """ Save textualFPathvariable variable.
        """
        self.__textualFPath = textualFPath
    def setTextualFVariableName(self, textualFVariableName):
        """ Save textualFVariableName variable.
        """
        self.__textualFVariableName = textualFVariableName
    def setTextualHPath(self, textualHPath):
        """ Save textualHPathvariable variable.
        """
        self.__textualHPath = textualHPath
    def setTextualHVariableName(self, textualHVariableName):
        """ Save textualFVariableName variable.
        """
        self.__textualHVariableName = textualHVariableName
    def setTextualVisualFPath(self, textualVisualFPath):
        """ Save textualVisualFPath variable.
        """
        self.__textualVisualFPath = textualVisualFPath
    def setTextualVisualFVariableName(self, textualVisualFVariableName):
        """ Save textualVisualFVariableName variable.
        """
        self.__textualVisualFVariableName = textualVisualFVariableName
    def setVisualFPath(self, visualFPath):
        """ Save visualFPathvariable variable.
        """
        self.__visualFPath = visualFPath
    def setVisualFVariableName(self, visualFVariableName):
        """ Save visualFVariableName variable.
        """
        self.__visualFVariableName = visualFVariableName
    def setVisualHPath(self, visualHPath):
        """ Save visualHPathvariable variable.
        """
        self.__visualHPath = visualHPath
    def setVisualHVariableName(self, visualHVariableName):
        """ Save visualFVariableName variable.
        """
        self.__visualHVariableName = visualHVariableName
    def setVisualTextualFPath(self, visualTextualFPath):
        """ Save visualtextualFPath variable.
        """
        self.__visualTextualFPath = visualTextualFPath
    def setVisualTextualFVariableName(self, visualTextualFVariableName):
        """ Save textualVisualFVariableName variable.
        """
        self.__visualTextualFVariableName = visualTextualFVariableName


class TagsConfig:

    def __init__(self,topWords,LTNamesTop,LTNamesSize):
        """FALTA DOCUMENTAR"""
        self.topWords = topWords
        self.LTNamesTop = LTNamesTop
        self.LTNamesSize = LTNamesSize

class ZentityPathsConfig:

    def __init__(self,codeStoragePath,zxmlFilesPath,xmlInfoPath):
        """FALTA DOCUMENTAR"""
        self.codePath = codeStoragePath
        self.zxmlPath = zxmlFilesPath
        self.xmlPath = xmlInfoPath

