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
        representativewords: array or matrix, 
            Basis of the Latent Topic.
        representativeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documnets.
        resumeWords: array or matrix, 
            Basis of the Latent Topic on the Asymmetric Factorization.
        resumeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documnets on the Asymmetric Factorization.
	
        Attributes
        ----------
        id : int,
            ID of the LatentTopic
        name: String 
            Name of the LatentTopic.
        belongingVector: array or matrix, 
            Vector of belonging degrees of each Document to the Latent Topic.
        representativewords: array or matrix, 
            Basis of the Latent Topic.
        representativeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documnets.
        resumeWords: array or matrix, 
            Basis of the Latent Topic on the Asymmetric Factorization.
        resumeDocuments: array or matrix, 
            Basis of the Latent Topic in terms of the documnets on the Asymmetric Factorization.	
    """   
    def __init__(self, ids, name, belongingVector, representativewords, representativeDocuments,ResumeWords,ResumeDocuments):
        self.__id = ids
        self.__name = name
        self.__belongingVector = belongingVector
        self.__representativewords=representativewords
        self.__representativeDocuments=representativeDocuments
	self.__resumeWords=ResumeWords
	self.__resumeDocuments=ResumeDocuments
        
    
    
    #Getters for each attributes
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getBelongingVector(self, id):
        return self.__belongingVector.get(id)
    def getRepresentativewords(self, id):
        return self.__representativewords.get(id)
    def getRepresentativeDocuments(self, id):
        return self.__representativeDocuments.get(id)
    def getResumeWords(self, id):
        return self.__resumeWords.get(id)
    def getResumeDocuments(self,id):
        return self.__resumeDocuments.get(id)

    
   
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
            Dictionay of Documents where the key is the id of the document and the object is the position of the document on the matrixes.   
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
        return self.__nabreviature
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
        self.__namse=name
    def setAbreviature(self,Abreviature):
        self.__abreviature=Abreviature



class Document:
    def __init__(self,ids):
        self.__id = ids
        
    def getId(self):
        return self.__id
    def setId(self,ids):
        self.__id=ids


