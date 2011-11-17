class LatentTopic:
    """  	
        ControlLatentTopic(id, H, F1, W1, F2, W2, CTLT)
    
        RESUME

	
        Parameters
        ----------
        id : int,
            ID of the LatentTopic
        name: String 
            Name of the LatentTopic.
        belongingVector: array or matrix, 
            Vector of belonging degrees of each Document to the Latent Topic.
        representativeWords: array or matrix, 
            Basis of the Latent Topic.
        sortedIndexRepresentativeWords: array or matrix, 
            Vector of position index of the representativeWords in decreasing order.
        representativeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documents.
        sortedIndexRepresentativeDocuments: array or matrix, 
            Vector of position index of the representativeDocuments in decreasing order.
        resumeWords: array or matrix, 
            Basis of the Latent Topic on the Asymmetric Factorization.
        sortedIndexResumeWords: array or matrix, 
            Vector of position index of the resumeWords in decreasing order.
        resumeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documents on the Asymmetric Factorization.
        sortedIndexResumeDocuments: array or matrix, 
            Vector of position index of the resumeDocuments in decreasing order.
	
        Attributes
        ----------
        id : int,
            ID of the LatentTopic
        name: String 
            Name of the LatentTopic.
        belongingVector: array or matrix, 
            Vector of belonging degrees of each Document to the Latent Topic.
        representativeWords: array or matrix, 
            Basis of the Latent Topic.
        sortedIndexRepresentativeWords: array or matrix, 
            Vector of position index of the representativeWords in decreasing order.
        representativeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documents.
        sortedIndexRepresentativeDocuments: array or matrix, 
            Vector of position index of the representativeDocuments in decreasing order.
        resumeWords: array or matrix, 
            Basis of the Latent Topic on the Asymmetric Factorization.
        sortedIndexResumeWords: array or matrix, 
            Vector of position index of the resumeWords in decreasing order.
        resumeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documents on the Asymmetric Factorization.
        sortedIndexResumeDocuments: array or matrix, 
            Vector of position index of the resumeDocuments in decreasing order.	
    """   
    def __init__(self, ids, name, belongingVector, representativeWords, sortedIndexRepresentativeWords, representativeDocuments, sortedIndexRepresentativeDocuments, resumeWords, sortedIndexResumeWords, resumeDocuments, sortedIndexResumeDocuments):
        self.__id = ids
        self.__name = name
        self.__belongingVector = belongingVector
        self.__representativeWords = representativeWords
        self.__sortedIndexRepresentativeWords = sortedIndexRepresentativeWords
        self.__representativeDocuments = representativeDocuments
        self.__sortedIndexRepresentativeDocuments = sortedIndexRepresentativeDocuments
	self.__resumeWords = resumeWords
        self.__sortedIndexResumeWords = sortedIndexResumeWords
	self.__resumeDocuments = resumeDocuments
        self.__sortedIndexResumeDocuments = sortedIndexResumeDocuments
        
    
    
    #Getters for each attributes
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getBelongingVector(self, id):
        return self.__belongingVector[id]
    def getRepresentativeWords(self, id):
        return self.__representativeWords[id]
    def getSortedIndexRepresentativeWords(self):
        return self.__sortedIndexRepresentativeWords
    def getRepresentativeDocuments(self, id):
        return self.__representativeDocuments[id]
    def getSortedIndexRepresentativeDocuments(self):
        return self.__sortedIndexRepresentativeDocuments
    def getResumeWords(self, id):
        return self.__resumeWords[id]
    def getSortedIndexResumeWords(self):
        return self.__sortedIndexResumeWords
    def getResumeDocuments(self,id):
        return self.__resumeDocuments[id]
    def getSortedIndexResumeDocuments(self):
        return self.__sortedIndexResumeDocuments

    
   
    #set method for the only attribute that can change.
    def setName(self,name):
        self.__name=name
   

class TypeLatentTopic:
    """
        ControlTypeLatentTopic(id, name, abreviature, LD, H, F1, W1, F2, W2)
    
        RESUME
	
        Parameters
        ----------
        id : int,
            ID of the TypeLatentTopic
        name: String 
            Name of the TypeLatentTopic. 
        abreviature: String
            Abreviature of the TypeLatentTopic.
        Dictionary: dict 
            Dictionay of Documents where the key is the id of the document and the object is the position of the document on the matrixes.
        

        Attributes
        ----------
        id : int,
            ID of the TypeLatentTopic
        name: String 
            Name of the TypeLatentTopic. 
        abreviature: String
            Abreviature of the TypeLatentTopic.
        Dictionary: dict
            Dictionary of Documents where the key is the id of the document and the object is the position of the document on the matrixes.   
    """
    def __init__(self,ids,name,abreviature,Dictionary):
        self.__id = ids
        self.__name = name
        self.__abreviature=abreviature
        self.__Dictionary =Dictionary



    #Getters for each attributes
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getAbreviature(self):
        return self.__abreviature
    def getDictionary(self,id):
        return self.__Dictionary.get(id)
    


    def getSizeDictionary(self):
        """ Return the size of the dictionary. 
        """
        return len(self.__Dictionary)
    
    

    #Setters
    def setId(self,ids):
        self.__id=ids
    def setName(self,name):
        self.__name=name
    def setAbreviature(self,Abreviature):
        self.__abreviature=Abreviature



class Document:
    def __init__(self,ids):
        self.__id = ids
        
    def getId(self):
        return self.__id
    def setId(self,ids):
        self.__id=ids


